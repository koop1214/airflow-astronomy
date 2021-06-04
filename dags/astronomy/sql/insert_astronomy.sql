{% set row = ti.xcom_pull(task_ids="get_astronomy") %}
INSERT INTO
    astronomy (metar, date, sunrise, sunset, moonrise, moonset, moon_phase, moon_illumination)
VALUES (
        '{{ params.metar_code }}',
        '{{ execution_date.strftime("%Y-%m-%d") }}',
        '{{ row["sunrise"] }}',
        '{{ row["sunset"] }}',
        '{{ row["moonrise"] }}',
        '{{ row["moonset"] }}',
        '{{ row["moon_phase"] }}',
        {{ row["moon_illumination"] }}
        )
ON CONFLICT (metar, date) DO
    UPDATE
        SET
            sunrise = excluded.sunrise,
            sunset = excluded.sunset,
            moonrise = excluded.moonrise,
            moonset = excluded.moonset,
            moon_phase = excluded.moon_phase,
            moon_illumination = excluded.moon_illumination
            ;
