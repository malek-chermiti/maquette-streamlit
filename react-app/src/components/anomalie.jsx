import React from "react";
import "./anomalie.css";

function Anomalie({ anomalies = [] }) {
    const critical =
        anomalies.filter(
            a => a.severite === "critique"
        ).length;

    const open =
        anomalies.filter(
            a => a.statut === "ouverte"
        ).length;

    const resolved =
        anomalies.filter(
            a => a.statut === "resolue"
        ).length;

    return (
        <div className="anomaly-container">
            <h1>
                ⚠️ TOWERMIND - Anomalies
            </h1>

            <div className="kpi-container">
                <div className="kpi critical">
                    <span>CRITICAL</span>
                    <strong>{critical}</strong>
                </div>

                <div className="kpi open">
                    <span>OPEN</span>
                    <strong>{open}</strong>
                </div>

                <div className="kpi resolved">
                    <span>RESOLVED</span>
                    <strong>{resolved}</strong>
                </div>
            </div>

            <div className="table-box">
                <h2>📋 Anomalies List</h2>

                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>PROJECT</th>
                            <th>ELEMENT</th>
                            <th>TYPE</th>
                            <th>SEVERITY</th>
                            <th>STATUS</th>
                            <th>ACTIONS</th>
                        </tr>
                    </thead>

                    <tbody>
                        {anomalies.map(a => (
                            <tr key={a.id}>
                                <td>{a.id}</td>
                                <td>{a.projet_nom || "-"}</td>
                                <td>{a.element_id}</td>
                                <td>{a.type_anomalie}</td>
                                <td>
                                    <span className="badge">
                                        {a.severite}
                                    </span>
                                </td>
                                <td>{a.statut}</td>
                                <td>
                                    <button className="edit-btn">✏️</button>
                                    <button className="delete-btn">🗑</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default Anomalie;