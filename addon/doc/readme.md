# reportOnce

reportOnce is a small NVDA add-on that stops NVDA from repeating object position information (for example "3 of 10") for every object in the same group.

### Usage

1. Open NVDA settings and go to the Object Presentation category.
2. Make sure "Report object position information" is checked. The new checkbox only appears when it is.
3. Check "Report position information only once".

When enabled, NVDA reports position information when you move to an object, and does not repeat it while you move between objects with the same parent, role and level. It is announced again when you enter a different group or come back to one.

When the checkbox is not checked, NVDA behaves exactly as before.

### Notes

- Pressing NVDA+Tab always reports the full information.
- Currently covers focus changes and object navigation. Browse mode is not affected.

### Requirements

NVDA 2024.1 or later.