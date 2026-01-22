# PyUnit-Converter
A command-line utility for performing standard metric-to-imperial conversions.

## 🛠 Software Development Life Cycle (SDLC)

**Name:** Jimoh Olamilekan Ridwanlah
**Matric No.:** 25/18456
**Course:** Computer Science

### Phase 1: Requirements Definition
The objective was to build a lightweight tool to assist with common engineering conversions.
**Functional Specifications:**
1.  **Scope:** The system must handle two primary categories: Length and Weight.
2.  **Precision:** Output results must be rounded to 4 decimal places for engineering accuracy.
3.  **Operations:**
    *   Convert Kilometers (km) ↔ Miles (mi).
    *   Convert Kilograms (kg) ↔ Pounds (lbs).
4.  **Stability:** The system must handle non-numeric inputs without crashing.

### Phase 2: System Design
The architecture uses a functional approach with distinct handlers for each measurement type to ensure modularity.

*   **Logic Modules:**
    *   `process_length_conversion()`: Handles the logic for distance (Factor: 1 km = 0.621371 mi).
    *   `process_weight_conversion()`: Handles the logic for mass (Factor: 1 kg = 2.20462 lbs).
*   **Controller:**
    *   `start_interface()`: The main entry point that routes user selection to the appropriate logic module.
*   **Data Flow:** User Menu -> Selection -> Numeric Input -> Calculation -> Formatted Output.

### Phase 3: Implementation
The application was written in Python 3 using standard arithmetic operators.
*   **Conversion Factors:** Hardcoded constants were used for reliability (e.g., `0.621371`).
*   **Input Handling:** A `try-except` block is placed within the specific conversion functions to validate the `value_to_convert`.
*   **User Experience:** Clear text prompts guide the user through the sub-menus (e.g., "1 for Km->Miles, 2 for Miles->Km").

### Phase 4: Testing & Verification
**Test Suite Results:**
1.  **Length Test:** Converted 10 Kilometers to Miles.
    *   *Expected:* ~6.2137
    *   *Actual:* 6.2137 (Pass)
2.  **Weight Test:** Converted 50 Pounds to Kilograms.
    *   *Expected:* ~22.6796
    *   *Actual:* 22.6796 (Pass)
3.  **Error Handling:** Entered "Hello" as the value to convert.
    *   *Result:* System output "Invalid format" and returned to the main menu (Pass).

### Phase 5: Deployment
The tool is compiled into a single script: `unit_converter.py`. It is platform-independent and runs in any standard terminal environment.

---

## ⚙️ Execution Instructions

1.  Ensure Python 3 is installed.
2.  Run the script:
    ```bash
    python unit_converter.py
    ```
3.  Select a category (Length or Weight) and follow the prompts.
