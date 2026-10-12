Capstone Proposal
Path
AfyaPlus Module 4 Capstone: Integrated AI Health Operations System

Problem
Clinic operations teams need a system that can receive authenticated patient triage requests, retrieve grounded answers from approved health documents (RAG), route requests through an agent capable of calling logistics tools, and return validated JSON responses securely.

The system should support authenticated access, version-controlled prompts and models, and evaluation reporting. A multimodal lane is optional and currently deferred.

Current minimum product: deterministic grounded lookup over synthetic clinic stock, an authenticated local API, and one in-process MCP tool stub. Approved clinical-document retrieval and live model calls are future work.

Success this week means delivering a working end-to-end system with documented architecture, passing tests, security checks, and a presentation-ready packet.

Dataset
fixtures/triage_messages_sample.jsonl

Approximately 300 synthetic triage rows for teaching purposes.

No production data will be used.

No patient PII will be stored.

Do not use millions of rows.

Milestones
Monday: proposal.md, skill_matrix.md, integration_map.json, base service returns 200 from /health
Tuesday: unit tests, integration tests, security smoke tests, evaluation pipeline, CI verification
Thursday: documentation, peer review, presentation slides, demo script
Week 12 Monday: capstone presentation and system demonstration
Out of Scope
Training a new foundation model
Live patient data collection
Production-scale datasets
Live PII crawling
Silent rewriting of records
Optional Multimodal Lane
Week 10 mismatch detection will be adapted to AfyaPlus by comparing structured intake descriptions against image or attachment metadata and flagging potential mismatches for human review.

The system will only flag for review and will never automatically rewrite records.