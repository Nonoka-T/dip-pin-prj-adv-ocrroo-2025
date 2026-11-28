/**
 * Personalisation: user can choose the text size of the code.
 choice is saved in the browser so it's kept next time.
 */
class UserPreferences {
    constructor() {
        this.storageKey = "ocrroo-text-size";
        this.sizes = {
            "small": "16px",
            "medium": "20px",
            "large": "28px",
            "ex-large": "36px"
        };
    }

    /** Read saved size, use "medium" if nothing is saved yet. */
    loadTextSize() {
        const saved = localStorage.getItem(this.storageKey);
        if (saved in this.sizes) {
            return saved;
        }
        return "medium";
    }

    /**save the size and show it on the page */
    saveTextSize(sizeName) {
        localStorage.setItem(this.storageKey, sizeName);
        this.applyTextSize(sizeName);
    }

    /** Change css variable used by code area */
    applyTextSize(sizeName) {
        document.documentElement.style.setProperty("--code-size", this.sizes[sizeName]);
    }
}