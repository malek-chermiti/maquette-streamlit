import hashlib
import json
from pathlib import Path

import streamlit as st

import services.auth_service as auth_service
from config import AUTH_STORE_PATH


def _safe_rerun():
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()


def _register_user(first_name: str, last_name: str, email: str, password: str) -> dict:
    register = getattr(auth_service, "register_user", None)
    if register:
        return register(first_name, last_name, email, password)

    normalized_email = email.strip().lower()
    auth_store_file = Path(__file__).resolve().parent / AUTH_STORE_PATH
    auth_store_file.parent.mkdir(parents=True, exist_ok=True)

    if auth_store_file.exists():
        try:
            users = json.loads(auth_store_file.read_text(encoding="utf-8") or "[]")
        except Exception:
            users = []
    else:
        users = []

    if any(user.get("email", "").strip().lower() == normalized_email for user in users):
        return {
            "ok": False,
            "message": "Un compte existe deja avec cette adresse email.",
        }

    users.append(
        {
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "email": normalized_email,
            "password_hash": hashlib.sha256(password.encode("utf-8")).hexdigest(),
        }
    )
    auth_store_file.write_text(json.dumps(users, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "ok": True,
        "message": "Inscription reussie. Vous pouvez maintenant vous connecter.",
    }


def _render_register_form():
    st.markdown(
        """
        <div class='login-brand'>
            <div class='login-icon'>SIGN UP</div>
            <div class='login-title'>Inscription</div>
            <div class='login-subtitle'>Creez votre compte avant la connexion</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("register_form", clear_on_submit=False):
        first_name = st.text_input("Prenom")
        last_name = st.text_input("Nom")
        email = st.text_input("Email")
        password = st.text_input("Mot de passe", type="password")
        password_confirm = st.text_input("Confirmer le mot de passe", type="password")
        submitted = st.form_submit_button("S'inscrire", use_container_width=True)

    if submitted:
        if not email.strip() or not password:
            st.error("L'email et le mot de passe sont obligatoires.")
        elif password != password_confirm:
            st.error("Les deux mots de passe doivent etre identiques.")
        else:
            result = _register_user(first_name, last_name, email, password)
            if result.get("ok"):
                st.session_state.login_email = email.strip()
                st.session_state.registration_done = True
                st.session_state.auth_step = "login"
                st.success("Inscription reussie. Vous pouvez maintenant vous connecter.")
                _safe_rerun()
            else:
                st.error(result.get("message", "L'inscription a echoue."))


def _render_login_form():
    st.markdown(
        """
        <div class='login-brand'>
            <div class='login-icon'>LOGIN</div>
            <div class='login-title'>Connexion</div>
            <div class='login-subtitle'>Etape 2 : connexion apres inscription</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    default_email = st.session_state.get("login_email", "")

    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("Email", value=default_email)
        password = st.text_input("Mot de passe", type="password")
        submitted = st.form_submit_button("Se connecter", use_container_width=True)

    if submitted:
        if not email.strip() or not password:
            st.error("Veuillez saisir votre email et votre mot de passe.")
        else:
            result = auth_service.login(email, password)

            if isinstance(result, dict) and result.get("ok"):
                auth_service.save_token(
                    result.get("access_token", "local-token"),
                    email=email.strip(),
                    auth_source=result.get("source", "local"),
                )
                st.success("Connexion reussie")
                _safe_rerun()
                return

            message = "Erreur de connexion."
            if isinstance(result, dict):
                message = result.get("message", message)
            st.error(message)


def show_auth():
    if not st.session_state.get("authenticated", False):
        if not st.session_state.get("registration_done", False):
            st.session_state.auth_step = "register"
        elif st.session_state.get("auth_step") not in {"register", "login"}:
            st.session_state.auth_step = "login"

    st.markdown('<div class="login-page">', unsafe_allow_html=True)
    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    if st.session_state.get("auth_step") == "register":
        _render_register_form()
    else:
        _render_login_form()

    st.markdown("</div></div>", unsafe_allow_html=True)
