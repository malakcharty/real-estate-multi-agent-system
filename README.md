
# Real Estate Multi-Agent System

A real estate analysis prototype built with **Python and Agno**. The system uses three specialized AI agents to search, compare, and recommend properties based on user criteria.

> **Note:** This project uses fictional real estate listings for demonstration purposes.

## Overview

The system is built around an **Agno Team Leader** that coordinates three specialized agents.

| Agent | Responsibility |
|---|---|
| Property Search Agent | Searches for properties matching user criteria |
| Pricing Analysis Agent | Compares prices per square meter |
| Recommendation Agent | Ranks properties using weighted scoring |

The Team Leader delegates tasks to the appropriate agents and combines their results into a final recommendation.

## Architecture

```text
                    User Request
                         |
                         v
                   Agno Team Leader
                   (Coordinate Mode)
                         |
             +-----------+-----------+
             |           |           |
             v           v           v
          Property     Pricing   Recommendation
           Search      Analysis      Agent
            Agent       Agent
             |           |           |
             v           v           v
         Search Tool  Pricing Tool  Scoring Tool
             |           |           |
             +-----------+-----------+
                         |
                         v
                   CSV Dataset
                Pydantic Validation
                         |
                         v
                 Final Recommendation
```

## Key Features

- Multi-agent coordination and task delegation with Agno
- Property search based on user criteria
- Price-per-square-meter comparison
- Weighted recommendation scoring
- CSV data validation with Pydantic
- Data anomaly detection
- Automated tests using pytest

## Tech Stack

**Python 3.12** · **Agno** · **OpenAI-compatible LLM** · **Pydantic** · **CSV** · **pytest**

## Project Structure

```text
real-estate-multi-agent-system/
├── agents/
│   ├── property_search_agent.py
│   ├── pricing_agent.py
│   └── recommendation_agent.py
├── teams/
│   └── real_estate_team.py
├── tools/
│   ├── property_tools.py
│   ├── pricing_tools.py
│   ├── recommendation_tools.py
│   ├── anomaly_tools.py
│   └── data_loader.py
├── models/
│   └── property.py
├── data/
│   └── properties.csv
├── tests/
│   ├── test_property_tools.py
│   └── test_anomaly_tools.py
├── .gitignore
└── README.md
```

## Usage

Run the multi-agent system:

```bash
python -m teams.real_estate_team
```

The example request searches for apartments in Casablanca with:

- Maximum budget: 2,500,000 MAD
- Minimum bedrooms: 3
- Minimum surface area: 100 m²

The Team Leader coordinates property search, pricing analysis, and recommendation.

## Recommendation Scoring

Properties are ranked using a weighted scoring system implemented in Python.

| Criterion | Weight |
|---|---:|
| Price per m² | 40% |
| Surface area | 25% |
| Total price | 20% |
| District preference | 15% |
| **Total** | **100%** |

Scores are relative to the properties being compared and do not represent real market valuations.

## Data Validation

Property data is loaded from a CSV file and validated with **Pydantic**.

An additional anomaly detection tool identifies:

- Invalid property data
- Duplicate property identifiers
- Prices per m² outside configurable thresholds

The anomaly detection tool runs independently from the multi-agent Team.

## Testing

Automated tests are implemented with **pytest**.

Run all tests:

```bash
python -m pytest tests/ -v
```

The test suite covers:

- Property search
- Search with no results
- Price comparison
- Recommendation scoring
- Data anomaly detection

## Limitations & Future Improvements

This project is a prototype based on fictional property data.

Current limitations include the absence of live real estate listings and the use of predefined scoring weights.

Possible improvements:

- Real estate API or database integration
- Session management and conversation history
- Advanced Agno Workflows
- Agent response evaluation
- User interface

## Purpose

This project was developed to put **Agno concepts into practice**, particularly AI Agents, Teams, Tools, task delegation, and structured data validation.
