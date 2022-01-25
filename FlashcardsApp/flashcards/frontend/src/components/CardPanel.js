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
        <Grid container spacing={2} spacing={2}>
          <Grid item xs={12}>
            <TextField
              id="outlined-basic"
              label="Front"
              variant="outlined"
              value={front}
              onChange={(e) => setFront(e.target.value)}
              multiline
              fullWidth
              margin="normal"
            />
          </Grid>

          <Grid item xs={12}>
            <TextField
              id="outlined-basic"
              label="Back"
              variant="outlined"
              value={back}
              onChange={(e) => setBack(e.target.value)}
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
                value={color}
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

          <Grid item xs={3}>
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
          </Grid>

          <Grid item xs={12}>
            <Grid container spacing={2} spacing={2} justifyContent="flex-end">
              <Grid item xs={2}>
                <Button
                  className="test"
                  color="secondary"
                  variant="outlined"
                  onClick={() => navigate(`../deck/${name}`)}
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
