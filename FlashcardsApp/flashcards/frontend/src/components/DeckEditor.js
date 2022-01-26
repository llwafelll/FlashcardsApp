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
  Grid,
  List,
  ListItem,
  ListItemText,
  ListButton,
  FormControl,
} from "@material-ui/core";
// import Select from '@mui/material/Select';

export default function CardAddPanel() {
  const navigate = useNavigate();

  const [deck, setDeck] = useState(null);
  const [name, setName] = useState("");
  const [color, setColor] = useState("nocolor");
  const [starred, setStarred] = useState(false);

  const { Dname } = useParams(null);

  function getDeck() {
      fetch(`/api/deck/${Dname}`)
      .then((response) => response.json())
      .then((data) => {
          setDeck(data);
          setName(data.name);
          setColor(data.color);
          setStarred(data.starred);
      })
  }

  useEffect(() => {
      getDeck();
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    const pendingDeck = { name, color, starred };
    console.log(JSON.stringify(pendingDeck))

    fetch(`/api/deck/${Dname}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(pendingDeck),
    });
  }

  return (
    deck && (
    <form onSubmit={handleSubmit} noValidate autoComplete="off">
      <Grid container spacing={2} spacing={2}>
        <Grid item xs={12}>
          <TextField
            id="outlined-basic"
            label="Deck's name"
            variant="outlined"
            value={name}
            onChange={(e) => setName(e.target.value)}
            multiline
            fullWidth
            margin="normal"
          />
        </Grid>

        <Grid item xs={3}>
          <FormControl fullWidth>
            <InputLabel id="card-color-label">color</InputLabel>
            <Select
              labelId="card-color-label"
              id="select-color"
              onChange={(e) => setColor(e.target.value)}
            >
              <MenuItem value={"red"}>red</MenuItem>
              <MenuItem value={"green"}>green</MenuItem>
              <MenuItem value={"yellow"}>yellow</MenuItem>
              <MenuItem value={"blue"}>blue</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={2} />

        <Grid item xs={3}>
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
        </Grid>

        <Grid item xs={12}>
          <Grid container spacing={2} spacing={2} justifyContent="flex-end">
            <Grid item xs={2}>
              <Button
                color="secondary"
                variant="outlined"
                onClick={() => navigate(`..`)}
              >
                Back
              </Button>
            </Grid>

            <Grid item xs={2}>
              <Button type="submit" color="primary" variant="contained">
                Save
              </Button>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </form>
    )
  );
}
