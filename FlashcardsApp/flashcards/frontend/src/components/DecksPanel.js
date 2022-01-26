import React, { Component } from "react";
import {
  Button,
  List,
  ListItem,
  ListItemText,
  Typography,
  ListButton,
} from "@material-ui/core";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

export default function DecksPanel({ children }) {
  const navigate = useNavigate();

  //   use state zwraca 2 argumenty - pierwszy to value drugi to funkcja ktora go
  //   zniemia (jest zdefiniowana od razu)
  const [decks, setDecks] = useState(null);

  function getDecks() {
    fetch("/api/deck/")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setDecks(data);
      });
  }
  useEffect(() => {
    getDecks();
  }, []);

  return (
    <div>
      <Typography variant="h4" gutterBottom component="div">
        Decks
      </Typography>
      <Button
        variant="contained"
        color="secondary"
        onClick={() => navigate(`/deck`)}
      >
        new deck
      </Button>
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
              <Button
                color="secondary"
                variant="outlined"
                onClick={() => {
                  fetch(`../api/deck/${deck.name}`, { method: "DELETE" }).then(
                    (response) => {
                      if (response.ok) {
                        getDecks();
                      }
                    }
                  );
                }}
              >
                Delete
              </Button>
            </ListItem>
          ))}
      </List>
    </div>
  );
}
