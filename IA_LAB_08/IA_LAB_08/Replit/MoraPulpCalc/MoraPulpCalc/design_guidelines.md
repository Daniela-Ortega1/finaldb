# MORITA - Blackberry Pulp Yield Calculator Design Guidelines

## Design Approach

**Selected Approach:** Design System - Material Design inspired
**Justification:** This is a utility-focused production tool requiring clarity, efficiency, and mobile-friendly operation for potential field use. The agricultural/production context demands straightforward functionality over visual flair.

## Layout & Structure

**Single-Page Layout:**
- Centered card-based design with max-w-2xl container
- Vertical flow: Header → Form → Results → Footer
- Generous padding (p-8 to p-12 on desktop, p-6 on mobile)
- Card elevated with shadow (shadow-lg) for depth

**Spacing System:**
Use Tailwind units: 2, 4, 6, 8, 12, 16 for consistent rhythm
- Form field spacing: space-y-6
- Section spacing: mb-8 to mb-12
- Inner component padding: p-4 to p-6

## Typography

**Font Stack:**
- Primary: 'Inter' or 'Plus Jakarta Sans' from Google Fonts
- Fallback: system-ui, sans-serif

**Hierarchy:**
- App Title (H1): text-3xl md:text-4xl, font-bold
- Section Headers (H2): text-xl md:text-2xl, font-semibold
- Labels: text-sm md:text-base, font-medium
- Input Text: text-base md:text-lg
- Results Display: text-2xl md:text-3xl, font-bold
- Helper Text: text-sm

## Component Library

**Form Components:**
- Text inputs with labels above, full-width with rounded-lg borders
- Input height: h-12 to h-14 for easy touch targets
- Focused state: ring-2 offset treatment
- Error states: border change with helper text below
- Number inputs with step="0.01" for decimal precision

**Button:**
- Primary CTA: Full-width or auto-width, rounded-lg, h-12
- Text: font-semibold, uppercase tracking-wide
- Icon support for calculate action

**Results Display:**
- Card-based results section with rounded-lg, p-6
- Two-column grid (md:grid-cols-2) for yield and loss metrics
- Large numerical display with units clearly labeled
- Icon indicators for each metric (chart/percentage icons from Heroicons)

**Header:**
- Project branding "MORITA" prominently displayed
- Subtitle: "Calculadora de Rendimiento de Pulpa de Mora"
- Optional berry/fruit icon from Heroicons

**Footer:**
- Compact, text-center, text-sm
- Project information or credits

## Icons

**Library:** Heroicons (via CDN)
**Usage:**
- Calculator icon for submit button
- Chart bar icon for yield result
- Percentage icon for loss result
- Berry/fruit icon for header (if available, else use leaf)

## Responsive Behavior

**Mobile-First Approach:**
- Single column layout base
- Stack all elements vertically
- Full-width inputs and buttons
- Results grid stacks to single column on mobile

**Breakpoints:**
- Mobile: Base (< 768px)
- Tablet/Desktop: md (≥ 768px)

## Validation & Feedback

**Input Validation:**
- Real-time validation on blur
- Required field indicators
- Minimum value constraints (> 0)
- Clear error messages in Spanish

**Calculation Display:**
- Results appear immediately below form
- Smooth transition when values update
- Percentage formatted to 2 decimal places
- Clear labeling: "Rendimiento" and "% de Merma"

## Accessibility

- Proper label-input associations
- Clear focus indicators on all interactive elements
- Semantic HTML structure (form, fieldset, legend)
- ARIA labels for icon-only elements
- Sufficient contrast ratios for all text
- Keyboard navigable

## Images

**No hero images required** - This is a utility application where function trumps form. The interface should be clean and distraction-free for production use.

## Animation

**Minimal animations only:**
- Subtle fade-in for results display (150ms)
- Form validation shake on error (optional)
- No decorative animations

---

**Design Philosophy:** Clean, professional, and immediately usable. The interface should feel like a reliable production tool that operators can trust for quick calculations in various environments, including potential mobile/field use.