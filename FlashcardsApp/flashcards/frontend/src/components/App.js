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

export default function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<DecksPanel />} />
                <Route path="/deck/:name" element={<DeckPanel />} />
                <Route path="/deck/:name/card/:id" element={<CardPanel /> } />
            </Routes>
        </Router>
    );
}

// const appDiv = document.getElementById("app");
// render(<App />, appDiv);
