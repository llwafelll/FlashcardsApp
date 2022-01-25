import  React, { Component } from "react";
import { render } from "react-dom";
import { 
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
} from "react-router-dom";

import DecksPanel from "./DecksPanel"
import DeckPanel from "./DeckPanel"
import CardPanel from "./CardPanel"
import CardAddPanel from "./CardAddPanel"

export default function App() {
    return (
        <div className="center">
            <Router>
                <Routes>
                    <Route path="/" element={<DecksPanel />} />
                    <Route path="/deck/:name" element={<DeckPanel />} />
                    <Route path="/deck/:name/card/:id" element={<CardPanel /> } />
                    <Route path="/deck/:name/card" element={<CardAddPanel /> } />
                </Routes>
            </Router>
        </div>
    );
}

// const appDiv = document.getElementById("app");
// render(<App />, appDiv);
