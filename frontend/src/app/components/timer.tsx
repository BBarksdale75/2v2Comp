import { Card } from '@mui/material';
import React, { useEffect, useState } from 'react';

const CountdownTimer = () => {
    const calculateTimeLeft = () => {
        const difference = +new Date('04/05/2024') - +new Date();
        let timeLeft = { days: 0, hours: 0, minutes: 0, seconds: 0 };

        if (difference > 0) {
            timeLeft = {
                days: Math.floor(difference / (1000 * 60 * 60 * 24)),
                hours: Math.floor((difference / (1000 * 60 * 60)) % 24),
                minutes: Math.floor((difference / 1000 / 60) % 60),
                seconds: Math.floor((difference / 1000) % 60),
            };
        }

        return timeLeft;
    };

    const [timeLeft, setTimeLeft] = useState(calculateTimeLeft());

    useEffect(() => {
        const timer = setTimeout(() => {
            setTimeLeft(calculateTimeLeft());
        }, 1000);

        return () => clearTimeout(timer);
    });

    return (
        <div>
            <Card variant='outlined'> 
            <h2 style={{
                
                fontSize: '2.5rem',
                color: '#ffdb4d',
                textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)',
                fontFamily: 'Arial, sans-serif',
                fontWeight: 'bold',
                textAlign: 'center'
            }}>
                {timeLeft.days} Days {timeLeft.hours} Hours {timeLeft.minutes} Minutes {timeLeft.seconds} Seconds
            </h2>
            </Card>
        </div>
    );
};

export default CountdownTimer;
