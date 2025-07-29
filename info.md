# HackRx 6.0 - LLM-Powered Intelligent Query-Retrieval System

## Overview

Design an LLM-Powered Intelligent Query–Retrieval System that can process large documents and make contextual decisions. The system should handle real-world scenarios in insurance, legal, HR, and compliance domains.

## Problem Statement

### Input Requirements
- Process PDFs, DOCX, and email documents
- Handle policy/contract data efficiently
- Parse natural language queries

### Technical Specifications
- Use embeddings (FAISS/Pinecone) for semantic search
- Implement clause retrieval and matching
- Provide explainable decision rationale
- Output structured JSON responses

### Sample Query
"Does this policy cover knee surgery, and what are the conditions?"

## System Architecture & Workflow

The system should implement the following components:

1. **Input Documents** - PDF Blob URL
2. **LLM Parser** - Extract structured query
3. **Embedding Search** - FAISS/Pinecone retrieval
4. **Clause Matching** - Semantic similarity
5. **Logic Evaluation** - Decision processing
6. **JSON Output** - Structured response

## Evaluation Parameters

Your solution will be evaluated based on:

### a) Accuracy
Precision of query understanding and clause matching

### b) Token Efficiency
Optimized LLM token usage and cost-effectiveness

### c) Latency
Response speed and real-time performance

### d) Reusability
Code modularity and extensibility

### e) Explainability
Clear decision reasoning and clause traceability

## API Documentation

### Base URL
**Local Development:** `http://localhost:8000/api/v1`

### Authentication
```
Authorization: Bearer 90e50cab23923f1b3c18cae7dff615036abb673c541a122ca87fdf4ea8dc3d51
```

### Required Endpoint

#### POST `/hackrx/run`

**Request Format:**
```json
POST /hackrx/run
Content-Type: application/json
Accept: application/json
Authorization: Bearer <api_key>

{
    "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
    "questions": [
        "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
        "What is the waiting period for pre-existing diseases (PED) to be covered?",
        "Does this policy cover maternity expenses, and what are the conditions?",
        "What is the waiting period for cataract surgery?",
        "Are the medical expenses for an organ donor covered under this policy?",
        "What is the No Claim Discount (NCD) offered in this policy?",
        "Is there a benefit for preventive health check-ups?",
        "How does the policy define a 'Hospital'?",
        "What is the extent of coverage for AYUSH treatments?",
        "Are there any sub-limits on room rent and ICU charges for Plan A?"
    ]
}
```

**Expected Response Format:**
```json
{
    "answers": [
        "A grace period of thirty days is provided for premium payment after the due date to renew or continue the policy without losing continuity benefits.",
        "There is a waiting period of thirty-six (36) months of continuous coverage from the first policy inception for pre-existing diseases and their direct complications to be covered.",
        "Yes, the policy covers maternity expenses, including childbirth and lawful medical termination of pregnancy. To be eligible, the female insured person must have been continuously covered for at least 24 months. The benefit is limited to two deliveries or terminations during the policy period.",
        "The policy has a specific waiting period of two (2) years for cataract surgery.",
        "Yes, the policy indemnifies the medical expenses for the organ donor's hospitalization for the purpose of harvesting the organ, provided the organ is for an insured person and the donation complies with the Transplantation of Human Organs Act, 1994.",
        "A No Claim Discount of 5% on the base premium is offered on renewal for a one-year policy term if no claims were made in the preceding year. The maximum aggregate NCD is capped at 5% of the total base premium.",
        "Yes, the policy reimburses expenses for health check-ups at the end of every block of two continuous policy years, provided the policy has been renewed without a break. The amount is subject to the limits specified in the Table of Benefits.",
        "A hospital is defined as an institution with at least 10 inpatient beds (in towns with a population below ten lakhs) or 15 beds (in all other places), with qualified nursing staff and medical practitioners available 24/7, a fully equipped operation theatre, and which maintains daily records of patients.",
        "The policy covers medical expenses for inpatient treatment under Ayurveda, Yoga, Naturopathy, Unani, Siddha, and Homeopathy systems up to the Sum Insured limit, provided the treatment is taken in an AYUSH Hospital.",
        "Yes, for Plan A, the daily room rent is capped at 1% of the Sum Insured, and ICU charges are capped at 2% of the Sum Insured. These limits do not apply if the treatment is for a listed procedure in a Preferred Provider Network (PPN)."
    ]
}
```

## Hosting Requirements

### Public URL
Your API must be publicly accessible
- Example: `https://your-domain.com/api/v1/hackrx/run`

### HTTPS Required
Secure connection mandatory for submission
- SSL certificate required

### Response Time
API should respond within reasonable time
- Timeout: < 30 seconds

## Recommended Tech Stack

- **Backend:** FastAPI
- **Vector DB:** Pinecone
- **LLM:** GPT-4
- **Database:** PostgreSQL

## Deployment Platforms

Choose from:
- Heroku
- Vercel
- Railway
- AWS/GCP/Azure
- Render
- DigitalOcean
- Netlify Functions
- Your own server

## Platform Journey

### Step 1: Team Management
Navigate to Dashboard → Team Management to view:
- Team name and details
- Current team members
- Quick submit button (top right)

### Step 2: Understanding Problem Statement
Access via Sidebar → Competition → Problem Statement
- Complete technical documentation
- API specifications
- Requirements and evaluation criteria

### Step 3: Making Submissions
Access via Dashboard → Submit or Sidebar → Competition → Submissions

**Required Fields:**
- **Webhook URL:** Your deployed `/hackrx/run` endpoint
- **Description (Optional):** Brief tech stack description

### Step 4: Tracking Performance
Access via Sidebar → Competition → My Submissions

**Key Metrics:**
- **Overall Score:** Total performance percentage
- **Accuracy Ratio:** Correct answers/total questions
- **Average Response Time:** Mean API response time

### Step 5: Checking Leaderboard
Access via Sidebar → Competition → Leaderboard
- Team rankings
- Performance metrics
- Real-time updates

## Pre-Submission Checklist

### API Requirements
- [ ] `/hackrx/run` endpoint is live
- [ ] HTTPS enabled and accessible
- [ ] Bearer token authentication ready
- [ ] Handles POST requests correctly

### Response Format
- [ ] Returns valid JSON response
- [ ] Includes success status field
- [ ] Contains processing information
- [ ] Response time under 30 seconds

### Testing
- [ ] API tested with sample data
- [ ] All endpoints working correctly
- [ ] Error handling implemented
- [ ] Documentation complete

## Submission Instructions

1. Submit your complete solution before the deadline
2. Include proper documentation and code comments
3. Ensure all requirements are met as per specifications
4. Test all API endpoints with sample data

## General Instructions

1. Read all instructions carefully before attempting
2. Use of AI tools and frameworks is encouraged
3. Submit your solution within the given time limit
4. Code should be well-documented and explainable

## Frequently Asked Questions

**Q: How often can I submit?**
A: You can submit as many times as you want. More submissions can improve your leaderboard ranking.

**Q: Why are some documents locked?**
A: Documents unlock after successful webhook submissions to encourage active participation.

**Q: How is my score calculated?**
A: Score = (Correct Answers / Total Questions) × 100. Each question is weighted equally.

## Technical Support

If you encounter any issues:
1. Refer to this comprehensive guide first
2. Check the problem statement for technical details
3. Contact the organizing team for assistance

---

**Good luck with your HackRx 6.0 submission!**