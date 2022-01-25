import React, { Component } from "react";
import { render } from "react-dom";
import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import red from "@mui/material/colors";

import {
  Button,
  List,
  ListItem,
  ListItemText,
  Grid,
  Typography,
  ListButton,
} from "@material-ui/core";

export default function DeckPanel() {
  const navigate = useNavigate();
  const [cards, setCards] = useState(null);
  const { name } = useParams(null);

  function getCards() {
    fetch(`/api/deck/${name}/card`)
      .then((response) => response.json())
      .then((data) => {
        setCards(data);
      });
  }
  useEffect(() => {
    getCards();
  }, []);

  return (

    <Grid container>

      <Typography variant="h4" gutterBottom component="div">
        Deck: {name}
      </Typography>
      <Grid item xs={12}>
        <Button
          variant="contained"
          color="secondary"
          onClick={() => navigate(`/deck/${name}/card`)}
        >
          Add
        </Button>

        <Button
          color="primary"
          variant="outlined"
          onClick={() => {
            navigate(`..`);
          }}
        >
          back
        </Button>
      </Grid>

      <Grid item xs={12}>
        <List>
          {cards &&
            cards.map((card) => (
              <ListItem key={card.id} button>
                <ListItemText primary={card.front} />
                <ListItemText primary={card.back} />
                <Button
                  color="primary"
                  variant="contained"
                  onClick={() => navigate(`/deck/${name}/card/${card.id}`)}
                >
                  Modify
                </Button>

                <Button
                  color="secondary"
                  variant="outlined"
                  onClick={() => {
                    fetch(`../api/deck/${name}/card/${card.id}`, {
                      method: "DELETE"
                    }).then((response) => {if (response.ok) {getCards()}})
                  }}
                >
                  delete
                </Button>
              </ListItem>
            ))}
        </List>
      </Grid>
    </Grid>
  );
}
