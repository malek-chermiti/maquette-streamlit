import hashlib
import json
import secrets
from pathlib import Path

import requests
import streamlit as st
from config import API_URL, AUTH_STORE_PATH


AUTH_STORE_FILE = Path(__file__).resolve().parent.parent / AUTH_STORE_PATH


def _ensure_auth_store() -> None:
    AUTH_STORE_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not AUTH_STORE_FILE.exists():
        AUTH_STORE_FILE.write_text("[]", encoding="utf-8")


def _load_users() -> list[dict]:
    _ensure_auth_store()
    try:
        content = AUTH_STORE_FILE.read_text(encoding="utf-8").strip()
        if not content:
            return []
        return json.loads(content)
    except Exception:
        return []


def _save_users(users: list[dict]) -> None:
    _ensure_auth_store()
    AUTH_STORE_FILE.write_text(
        json.dumps(users, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def _make_local_token(email: str) -> str:
    return f"local-{hashlib.sha256(f'{email}:{secrets.token_urlsafe(16)}'.encode('utf-8')).hexdigest()}"


def _find_user(email: str) -> dict | None:
    normalized_email = email.strip().lower()
    for user in _load_users():
        if user.get("email", "").strip().lower() == normalized_email:
            return user
    return None


def _backend_login(email: str, password: str) -> dict:
    """Try the backend login endpoint with common payload formats."""

    url = f"{API_URL}/login"
    payloads = [
        {"json": {"email": email, "password": password}},
        {"data": {"username": email, "password": password}},
        {"data": {"email": email, "password": password}},
    ]

    for payload in payloads:
        try:
            response = requests.post(url, timeout=5, **payload)
        except Exception:
            return {
                "ok": False,
                "source": "unreachable",
                "message": "Le backend est inaccessible et aucun compte local ne correspond à ces identifiants.",
            }

        if response.status_code == 200:
            try:
                data = response.json()
            except Exception:
                data = {}

            token = data.get("access_token")
            if token:
                return {
                    "ok": True,
                    "source": "backend",
                    "access_token": token,
                    "user": data.get("user", {"email": email}),
                }

    return {
        "ok": False,
        "source": "backend",
        "message": "Aucun compte local ne correspond à ces identifiants et le backend n'a pas validé la connexion.",
    }


# =========================
# 1. LOGIN (GET JWT)
# =========================
def login(email: str, password: str):
    """
    Appel API login
    Retourne response backend (JWT inclus si succès)
    """

    local_user = _find_user(email)
    if local_user and local_user.get("password_hash") == _hash_password(password):
        return {
            "ok": True,
            "source": "local",
            "access_token": _make_local_token(email),
            "user": {
                "email": local_user.get("email", email),
                "first_name": local_user.get("first_name", ""),
                "last_name": local_user.get("last_name", ""),
            },
        }

    return _backend_login(email, password)


def register_user(first_name: str, last_name: str, email: str, password: str):
    """Create a local user account for the Streamlit mock."""

    normalized_email = email.strip().lower()
    if not normalized_email or not password:
        return {
            "ok": False,
            "message": "L'email et le mot de passe sont obligatoires.",
        }

    users = _load_users()
    if _find_user(normalized_email):
        return {
            "ok": False,
            "message": "Un compte existe déjà avec cette adresse email.",
        }

    users.append(
        {
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "email": normalized_email,
            "password_hash": _hash_password(password),
        }
    )
    _save_users(users)

    return {
        "ok": True,
        "message": "Inscription réussie. Vous pouvez maintenant vous connecter.",
    }


# =========================
# 2. STOCKER TOKEN
# =========================
def save_token(token: str, email: str | None = None, auth_source: str = "local"):
    """
    Stocker JWT dans session Streamlit
    """

    st.session_state.token = token
    st.session_state.authenticated = True
    st.session_state.auth_source = auth_source
    if email:
        st.session_state.user_email = email


# =========================
# 3. RECUPERER TOKEN
# =========================
def get_token():

    return st.session_state.get("token", None)


# =========================
# 4. HEADERS AUTH (IMPORTANT)
# =========================
def get_auth_headers():

    token = get_token()

    if not token:
        return {}

    return {
        "Authorization": f"Bearer {token}"
    }


# =========================
# 5. APPEL API PROTEGEE
# =========================
def api_request(method: str, endpoint: str, data=None):
    """
    Envoie requête avec JWT au backend
    """

    url = f"{API_URL}{endpoint}"
    headers = get_auth_headers()

    try:

        if method.lower() == "get":

            response = requests.get(url, headers=headers)

        elif method.lower() == "post":

            response = requests.post(
                url,
                json=data,
                headers=headers
            )

        else:
            raise ValueError("Method not supported")

        return response

    except Exception as e:
        return None


# =========================
# 6. LOGOUT
# =========================
def logout():

    st.session_state.clear()
    st.session_state.authenticated = False