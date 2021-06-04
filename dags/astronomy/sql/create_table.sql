CREATE TABLE IF NOT EXISTS astronomy
(
    metar             VARCHAR(4)  NOT NULL,
    date              DATE        NOT NULL,
    sunrise           TIME        NOT NULL,
    sunset            TIME        NOT NULL,
    moonrise          TIME        NOT NULL,
    moonset           TIME        NOT NULL,
    moon_phase        VARCHAR(30) NOT NULL,
    moon_illumination INT         NOT NULL,
    UNIQUE (metar, date)
);
