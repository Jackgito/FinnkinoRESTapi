// Retrieves the schedules for Lappeenranta STRAND based on the date
const fetch = require('node-fetch');

async function getSchedule(areaId, date, nrOfDays = 1) {
    const baseUrl = 'https://www.finnkino.fi/xml/Schedule';
    const params = new URLSearchParams({
        area: areaId,
        dt: date,
        nrOfDays: nrOfDays
    });

    const url = `${baseUrl}?${params.toString()}`;

    try {
        const response = await fetch(url);

        if (response.ok) {
            const scheduleXml = await response.text();
            return scheduleXml;
        } else {
            throw new Error(`Error: ${response.status}`);
        }
    } catch (error) {
        console.error(error.message);
    }
}

const areaId = 1041; // Lappeenranta area ID
const date = '22.02.2024'; // Desired date
const nrOfDays = 1; // Number of days to retrieve the schedule

getSchedule(areaId, date, nrOfDays)
    .then(scheduleXml => console.log(scheduleXml))
    .catch(error => console.error(error));
