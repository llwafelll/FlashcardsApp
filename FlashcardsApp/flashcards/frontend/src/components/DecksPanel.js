import React, { Component } from "react";
import {
  Button,
  List,
  ListItem,
  ListItemText,
  ListButton,
} from "@material-ui/core";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react"

export default function DecksPanelv2({ children }) {
  const navigate = useNavigate();

//   use state zwraca 2 argumenty - pierwszy to value drugi to funkcja ktora go
//   zniemia (jest zdefiniowana od razu)
  const [realitems, setRealitems] = useState(null);

  useEffect(() => {
      fetch("/api/deck/")
      .then(response => response.json())
      .then(data => {
          console.log(data);
          setRealitems(data);
      })
  }, [])

  return (
    <div>
      <h3>Placeholder</h3>
      <List>
        {realitems && realitems.map((item) => (
          <ListItem key={item.name} button>
            <ListItemText primary={item.name} secondary={item.number_cards} />
            <Button color="primary">Learn</Button>
            <Button color="secondary" onClick={() => navigate("/api")}>
              Manage
            </Button>
          </ListItem>
        ))}
      </List>
    </div>
  );
}
