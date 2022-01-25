import React, { Component } from "react";
import {
  Button,
  List,
  ListItem,
  ListItemText,
  ListButton,
} from "@material-ui/core";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

export default function DecksPanel({ children }) {
  const navigate = useNavigate();

  //   use state zwraca 2 argumenty - pierwszy to value drugi to funkcja ktora go
  //   zniemia (jest zdefiniowana od razu)
  const [decks, setDecks] = useState(null);

  useEffect(() => {
    fetch("/api/deck/")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setDecks(data);
      });
  }, []);

  return (
    <div>
      <h3>Placeholder</h3>
      <List>
        {decks &&
          decks.map((deck) => (
            <ListItem key={deck.name} button>
              <ListItemText primary={deck.name} secondary={deck.number_cards} />
              <Button color="primary" variant="contained">
                Learn
              </Button>
              <Button
                color="secondary"
                variant="contained"
                onClick={() => navigate(`/deck/${deck.name}`)}
              >
                Manage
              </Button>
            </ListItem>
          ))}
      </List>
    </div>
  );
}
