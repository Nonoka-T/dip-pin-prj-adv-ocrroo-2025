/**
 * Client side validation for the time input, it runs in browser before any requests are sent to the server.
 */
class TimeValidator {
    constructor(duration) {
        this.duration = duration; // length of the video in seconds
    }

    /**
     * Return error message or an empty str if the time is valid.
     */
    validate(text) {
        const value = text.trim();

        if (value === "") {
            return "Please enter a time in seconds.";
        }

        const seconds = Number(value);

        if (Number.isNaN(seconds)) {
            return "Time must be a number, for example 42 or 42.5.";
        }
        if (seconds < 0) {
            return "Time cannot be less than 0.";
        }
        if (seconds >= this.duration) {
            const max = Math.floor(this.duration);
            return `The time must be less than the video length (${max} seconds).`;
        }

        return "";
    }
}