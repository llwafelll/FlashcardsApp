import React, { Component } from "react";
import { render } from "react-dom";
import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import {
  Button,
  TextField,
  Select,
  MenuItem,
  InputLabel,
  Checkbox,
  FormControlLabel,
  List,
  ListItem,
  ListItemText,
  ListButton,
  FormControl,
} from "@material-ui/core";
// import Select from '@mui/material/Select';

export default function CardPanel() {
  const navigate = useNavigate();
  const { name, id } = useParams(null);

  const [card, setCard] = useState(null);
  const [front, setFront] = useState("");
  const [back, setBack] = useState("");
  const [color, setColor] = useState("");
  const [starred, setStarred] = useState("");
  const [suspended, setSuspended] = useState("");

  const [age, setAge] = React.useState("");

  useEffect(() => {
    console.log(name);
    fetch(`/api/deck/${name}/card/${id}`)
      .then((response) => response.json())
      .then((data) => {
        setCard(data);
        setFront(data.front);
        setBack(data.back);
        setColor(data.color);
        setStarred(data.starred);
        setSuspended(data.suspended);
      });
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    const pendingCard = { front, back, color, starred, suspended };
    console.log(card);
    console.log(pendingCard);

    fetch(`/api/deck/${name}/card/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(pendingCard),
    });
  }

  return (
    card && (
      <form onSubmit={handleSubmit} noValidate autoComplete="off">
        <TextField
          id="outlined-basic"
          label="Front"
          variant="outlined"
          value={front}
          onChange={(e) => setFront(e.target.value)}
          multiline
          margin="normal"
        />
        <br />
        <TextField
          id="outlined-basic"
          label="Back"
          variant="outlined"
          value={back}
          onChange={(e) => setBack(e.target.value)}
          multiline
          margin="normal"
        />
        <br />
        <FormControl fullWidth>
          <InputLabel id="card-color-label">color</InputLabel>
          <Select
            labelId="card-color-label"
            id="select-color"
            value={color}
            onChange={(e) => setColor(e.target.value)}
          >
            <MenuItem value={"red"}>red</MenuItem>
            <MenuItem value={"green"}>green</MenuItem>
            <MenuItem value={"yellow"}>yellow</MenuItem>
            <MenuItem value={"blue"}>blue</MenuItem>
          </Select>
        </FormControl>
        <br />

        <FormControlLabel
          label="starred"
          control={
            <FormControlLabel
              control={
                <Checkbox
                  checked={starred}
                  onChange={(e) => setStarred(e.target.checked)}
                />
              }
            />
          }
        />
        <br />
        <FormControlLabel
          label="suspended"
          control={
            <FormControlLabel
              control={
                <Checkbox
                  checked={suspended}
                  onChange={(e) => setSuspended(e.target.checked)}
                />
              }
            />
          }
        />

        <br />
        <Button
          color="secondary"
          variant="outlined"
          onClick={() => navigate(`../deck/${name}`)}
        >
          Back
        </Button>
        <Button type="submit" color="primary" variant="contained">
          Save
        </Button>
      </form>
    )
  );
}
