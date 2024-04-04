/* eslint-disable react/no-unescaped-entities */
"use client";
import { Typography, Grid, Card, Paper } from "@mui/material";
import Image from "next/image";
import CountdownTimer from "./components/timer";

export default function Home() {
  return (
    <main className="flex min-h-screen items-center justify-center p-6">
        <Paper>
        <div className="space-y-6">
          <div className="bg-white dark:bg-black text-center p-6 rounded-lg shadow-lg">
            <Typography variant="h4" component="h1" gutterBottom>
              COMPETITION OVERVIEW
            </Typography>
            <Typography variant="body1">
              Welcome to the ultimate showdown in the digital realm where
              creativity meets code! Get ready to witness a thrilling 2v2 coding
              challenge that will set the virtual stage on fire. Join us as
              David and Hank, the dynamic duo known for their innovative
              solutions, face off against Tony and Brandon, the masterminds of
              efficiency and design. These formidable pairs will embark on an
              intense journey to build a groundbreaking web application under
              the ticking clock. With their skills put to the ultimate test,
              they'll push the boundaries of web development, exploring new
              technologies and collaborative strategies. Who will triumph as the
              architects of the future's web? Join us to find out which team's
              application will dazzle the digital world. It's not just a battle
              of codes; it's a quest for glory in the arena of innovation!
            </Typography>
          </div>
          <div className="bg-white dark:bg-black text-center p-6 rounded-lg shadow-lg">
            <Typography variant="h5" component="h2" gutterBottom>
              EVENT COUNTDOWN
            </Typography>
            <CountdownTimer />
          </div>
          <div className="bg-white dark:bg-black text-center p-6 rounded-lg shadow-lg">
            <Typography variant="h5" component="h2" gutterBottom>
              INCENTIVES:
            </Typography>
            <Typography>Losing team buys everyone dinner.</Typography>
          </div>
          <div className="bg-white dark:bg-black text-center p-6 rounded-lg shadow-lg">
            <Typography variant="h5" component="h2" gutterBottom>
              TERMS AND CONDITIONS:
            </Typography>
            <ul>
              <li>
                David and Tony must contribute at least 60% of the code to the
                repository. Failure to meet this requirement may result in a
                point reduction.
              </li>
              <li>
                Teams are required to fulfill a predetermined set of core
                requirements. Upon completion, they will be presented with a set
                of optional features and stretch goals to enhance their project.
              </li>
            </ul>
            <p>
              <strong>
                Stay tuned for further details on the scoring system and
                guidelines.
              </strong>
            </p>
          </div>
        </div>
    </Paper>
      </main>
  );
}
