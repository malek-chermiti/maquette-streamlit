# TOWERMIND — Refactored Project Structure

## Overview
This Streamlit application has been refactored following best practices with clean separation of concerns:
- **CSS/Styling** → Extracted to `style.css`
- **Constants & Config** → Centralized in `config.py`
- **UI Helper Functions** → Organized in `utils.py`
- **Application Logic** → Streamlined in `app.py`

## Project Structure

```
maquette streamlit/
├── app.py              # Main application with UI logic
├── config.py           # Constants, configurations, and data
├── utils.py            # Reusable UI helper functions
├── style.css           # All CSS styling
└── README.md           # This file
```

## File Descriptions

### `app.py` (Main Application)
- **Purpose**: Core application logic and page routing
- **Contains**: 
  - Page configuration
  - Sidebar navigation
  - 8 main pages with UI layouts
  - Direct Streamlit component calls
- **Benefits**: Clean, readable, focused on user experience

### `config.py` (Configuration)
- **Purpose**: Centralized constants and configuration
- **Contains**:
  - Page list and metadata
  - Navigation items
  - Filter options
  - Project references
  - AI agent definitions
  - Report sections
  - Color schemes
- **Benefits**: Easy to update content without touching code; DRY principle

### `utils.py` (UI Helpers)
- **Purpose**: Reusable UI component functions
- **Key Functions**:
  - `load_styles()` - Load CSS from file
  - `render_page_header()` - Consistent page titles
  - `render_kpi_row()` - KPI card layout
  - `render_card_with_title()` - Card components
  - `render_sidebar_header/footer()` - Sidebar sections
  - `render_agent_item()` - Agent pipeline items
  - `render_3d_viewer_placeholder()` - 3D viewer component
- **Benefits**: Consistency, code reuse, easier maintenance

### `style.css` (Styling)
- **Purpose**: All visual styling
- **Contains**:
  - Font imports and global styles
  - Component classes (.card, .placeholder, etc.)
  - Color definitions
  - Layout utilities
  - Responsive design
- **Benefits**: Separation of concerns, easier theming, cleaner HTML

## Usage

### Running the Application
```bash
streamlit run app.py
```

### Modifying Content
1. **Change page names/order**: Edit `PAGES` in `config.py`
2. **Update filter options**: Modify `FILTER_OPTIONS` dict
3. **Adjust colors**: Edit `COLORS` dict or update `style.css`
4. **Add new UI components**: Create helper functions in `utils.py`

### Adding a New Page
1. Add page to `PAGES` list in `config.py`
2. Create new `elif page == PAGES[n]:` block in `app.py`
3. Use helper functions from `utils.py` for consistency

## Best Practices Implemented

✅ **Separation of Concerns**
- Styling isolated from logic
- Constants separated from code
- UI helpers abstracted

✅ **Maintainability**
- No hardcoded strings
- Reusable components
- Clear file organization

✅ **Scalability**
- Easy to add pages
- Simple to update content
- Consistent patterns

✅ **Code Quality**
- DRY (Don't Repeat Yourself)
- Clear function names
- Proper documentation

## Dependencies
- `streamlit` - Web app framework
- Python 3.7+

## Future Improvements
- Extract pages into separate modules for very large apps
- Add state management (st.session_state)
- Implement page caching (@st.cache_data)
- Add unit tests for helper functions
- Implement custom hooks for data fetching
