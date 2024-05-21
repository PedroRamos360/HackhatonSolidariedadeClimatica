import React from 'react';
import { useNavigate } from 'react-router-dom';

export const LandingPage: React.FC = () => {
    const navigate = useNavigate(); 
    return (
        <div className="landing-page">
            <header className="jumbotron text-center">
                <h1>Ponto Seguro</h1>
                <p className="lead">Encontre abrigos e doe para pessoas afetadas pelas enchentes do Rio Grande do Sul.</p>
            </header>
            <main className="container">
                <section className="row">
                    <div className="col-md-6">
                        <div className="card">
                            <div className="card-body">
                                <h2 className="card-title">Econtre abrigos:</h2>
                                <p className="card-text">Localize abrigos perto de você ou pesquise uma localização específica.</p>
                                <button className="btn btn-primary" onClick={
                                    () => navigate('/mapa') 
                                }>Econtre abrigos</button>
                            </div>
                        </div>
                    </div>
                    <div className="col-md-6">
                        <div className="card">
                            <div className="card-body">
                                <h2 className="card-title">Doe agora:</h2>
                                <p className="card-text">Ajude pessoas afetadas pelas enchentes com sua doação.</p>
                                <button className="btn btn-primary">Doar</button>
                            </div>
                        </div>
                    </div>
                </section>
            </main>
            <footer className="text-center py-4">
                <p>&copy; 2024 Ponto Seguro.</p>
            </footer>
        </div>
    );
}; 

