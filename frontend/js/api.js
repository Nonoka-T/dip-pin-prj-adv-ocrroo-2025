/**
 * Talk to the Python (FastAPI) backend, backend is separate process so every request go over HTTP.
 */
class OcrApiClient {
    constructor(baseUrl, videoId) {
        this.baseUrl = baseUrl;
        this.videoId = videoId;
    }

    /** URL the <video> element uses to play the video */
    getStreamUrl() {
        return `${this.baseUrl}/video/${this.videoId}/stream`;
    }

    /** get the video information (fps, frame_count, duration_seconds) */
    async getVideoInfo() {
        const response = await fetch(`${this.baseUrl}/video/${this.videoId}`);
        if (!response.ok) {
            throw new Error("Video could not be found on the server.");
        }
        return await response.json();
    }

    /**ask the server to read the text in the frame at given time */
    async getTextAtTime(seconds) {
        const response = await fetch(
            `${this.baseUrl}/video/${this.videoId}/frame/${seconds}/ocr`
        );
        if (!response.ok) {
            throw new Error("Server could not read this frame");
        }
        const data = await response.json();
        return data.text.trim();
    }
}