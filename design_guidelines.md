# EduSubmit Pro Design Guidelines

## Design Approach
**System-Based Approach**: Material Design 3 with educational context adaptations
- Clean, professional interface prioritizing functionality and accessibility
- Consistent component library for scalable maintenance across complex role-based workflows

## Core Design Elements

### Color Palette
**Primary Colors:**
- Primary Blue: 214 88% 35% (professional academic blue)
- Primary Light: 214 65% 85% (light blue for backgrounds)
- White: 0 0% 100% (clean backgrounds)

**Supporting Colors:**
- Success Green: 142 76% 36% (approvals, submissions)
- Warning Orange: 25 95% 53% (pending states)
- Error Red: 0 84% 60% (rejections, overdue)
- Neutral Gray: 220 9% 46% (text, borders)

### Typography
**Font Stack**: Inter via Google Fonts
- Headings: 600 weight, sizes 24px-32px
- Body text: 400 weight, 16px
- Captions: 400 weight, 14px
- Labels: 500 weight, 14px

### Layout System
**Spacing Primitives**: Tailwind units of 2, 4, 6, 8, 12
- Container max-width: 1200px
- Card padding: p-6
- Section spacing: space-y-8
- Form field gaps: gap-4

## Component Library

### Navigation
- **Header**: Fixed top navigation with role-based menu items
- **Sidebar**: Collapsible department/course navigation for Faculty/Lecturers
- **Breadcrumbs**: Clear hierarchy showing Faculty > Department > Course paths

### Data Display
- **Assignment Cards**: Clean cards with status indicators, due dates, and action buttons
- **User Lists**: Table format with filter/search capabilities for Faculty oversight
- **Grade Displays**: Progress indicators and score visualizations

### Forms & Inputs
- **Registration Forms**: Multi-step with Faculty validation messaging
- **File Upload**: Drag-and-drop zones with supported format indicators
- **Grading Interface**: Slider inputs for rubric scores with text feedback areas

### Overlays
- **Modals**: Assignment details, approval confirmations
- **Toasts**: Success/error notifications for actions
- **Tooltips**: Helpful context for complex workflow steps

### Role-Specific Elements
- **Faculty Dashboard**: Overview cards showing pending approvals and system statistics
- **Student Portal**: Assignment feed with submission status tracking
- **Lecturer Interface**: Assignment creation wizard and grading tools

## Key Interactions
- **Registration Flow**: Clear error states when Faculty account doesn't exist
- **Approval Workflow**: Visual status progression for lecturer requests
- **File Handling**: Immediate upload feedback with progress indicators
- **Deadline Management**: Visual countdown timers and automatic state changes

## Notifications & Alerts

- Modern dropdown notification system with proper keyboard accessibility
- Real-time notification badges with red indicator for unread items  
- Role-specific notifications (Faculty: approvals, Lecturer: submissions, Student: grades)
- Notification categories with appropriate icons and color coding
- Interactive notification management (mark as read, dismiss, mark all read)
- Smooth transitions and hover effects with backdrop blur
- Toast notifications for success/error messages positioned in top-right
- Auto-dismiss success messages after 4-5 seconds
- Keep error messages until manually dismissed

## Accessibility & Responsiveness
- WCAG 2.1 AA compliance
- Mobile-first responsive design
- Keyboard navigation support with proper focus management
- Screen reader optimization for educational content hierarchy
- Tab-friendly interface elements with proper ARIA labels