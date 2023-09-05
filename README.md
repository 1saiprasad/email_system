# Event Email System

The Event Email System is a Django-based web application that automates the sending of emails on special occasions such as birthdays and work anniversaries. It retrieves event details from a database, generates personalized email content, and sends emails to employees on their special days.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [REST APIs](#rest-apis)
- [Scheduling Emails](#scheduling-emails)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatic email generation and sending based on event dates.
- Event data stored in the database.
- Email templates for various event types.
- Logging of email sending status and errors.
- REST APIs for admin access.
- Scheduled execution of email sending.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.x) installed.
- Django (3.x) installed.
- [Django REST framework](https://www.django-rest-framework.org/) installed (optional, for REST APIs).
- SMTP server details for sending emails.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/event-email-system.git
   cd event-email-system
