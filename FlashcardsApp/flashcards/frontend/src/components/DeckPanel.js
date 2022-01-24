import  React, { Component } from "react";
import { render } from "react-dom";
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import {
  Button,
  List,
  ListItem,
  ListItemText,
  ListButton,
} from "@material-ui/core";

export default function DeckPanel() {
    const [cards, setCards] = useState(null);
    const { name } = useParams(null);


    useEffect(() => {
        fetch(`/api/deck/${name}/card`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setCards(data);
        })
    }, [])

    return (
      <List>
        {cards && cards.map((card) => (
          <ListItem key={card.id} button>
            <ListItemText primary={card.front} />
            <ListItemText primary={card.back} />
          </ListItem>
        ))}
      </List>
    );
}