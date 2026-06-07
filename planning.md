# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

The domain that I chose was the quality of computer science professors at Stony Brook University. This is valuable knowledge for students that are deciding what professors they want to take courses with in future semesters. This knowledge is often hard to find through official channels because this information can be spread across a lot of different websites and through word of mouth only for some classes/professors.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | RateMyProfessors | Public rating and commments on Professor Ahmad Esmaili. | https://www.ratemyprofessors.com/professor/86020 |
| 2 | RateMyProfessors | Public rating and commments on Professor Praveen Tripathi. | https://www.ratemyprofessors.com/professor/2270244 |
| 3 | Reddit | Reddit forum on the Professor Daniel Benz. | https://www.reddit.com/r/SBU/comments/1gednkl/cse220_with_daniel_benz/ |
| 4 | Reddit | Reddit forum asking for advice on professors for introductory CS cources. | https://www.reddit.com/r/SBU/comments/yu8ro2/cse_101_profsadvice/ |
| 5 | Reddit | Reddit forum asking questions about taking a class with Professor Paul Fodor. | https://www.reddit.com/r/SBU/comments/jrqqyr/cse_114_with_paul_fodor/ |
| 6 | RateMyProfessors | Public rating and commments on Professor Robert Kelly. | https://www.ratemyprofessrs.com/professor/99650 |
| 7 | Reddit | Reddit forum asking about which CS professor to take a class with. | https://www.reddit.com/r/SBU/comments/vffod3/cse_214/ |
| 8 | Reddit | Reddit forum asking about which CS professor to take a class with. | https://www.reddit.com/r/SBU/comments/2rt1ca/cse_114_fodor_or_mckenna/ |
| 9 | RateMyProfessors | Public rating and commments on Professor Abid Malik. | https://www.ratemyprofessors.com/professor/2968856 |
| 10 | Reddit | Reddit forum asking about which CS professor to take a class with. | https://www.reddit.com/r/SBU/comments/160oo2n/cse_114_professor/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

The chunk size will start at around 300 tokens beacuase of the short responses on the chosen sources.

**Overlap:**

The overlap will start at around 50 tokens to prevent loss of context mainly when gathering information from Reddit posts.

**Reasoning:**

The two main sources that I chose to use are RateMyProfesssors and Reddit. Both of these sources contain short responses and selfcontained opionins. The chunks will be on the smaller size beacuase of the short responses and text on both sites. The overlap will prevent loss of context mainly when gathering information from Reddit posts.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
The embedding model that I will use will be all-MiniLM-L6-v2 via sentence-transformers for efficient embeddings and strong search performance.

**Top-k:**
I will start by retrieving the top-k = 5 chunks per query. This seems like a good starting point becuase it is a middle ground between retrieving too little and too many chunks.

**Production tradeoff reflection:**
If you were deploying this for real users, some possible tradeoffs would be:
1. Accuracy vs. Speed (the model may trade response speed for better responses)
2. Specific Terminology (the model might not understand SBU-specific terms)
3. Length of Context (some sources and forums may vary in length)

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Who is the better professor to take CSE101 with at Stony Brook? | Professor McDonnell. |
| 2 | Who is the most popular professor to take Computer Science classes with at Stony Brook? | Professor McDonnell or Professor Fodor. |
| 3 | What traits make a Computer Science professor unliked at Stony Brook? | Poor teaching style, not caring about students, improper attitude. |
| 4 | What do students say about Professor Ahmad Esmaili? | Mixed reviews, fair class structure, lectures are not engaging but he can teach concepts. |
| 5 | What professors are the best to take introductory Computer Science classes with at Stony Brook? | Professor McDonnell or Professor Fodor. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. One possible challenge is inconsistent data from the sources. This is because both RateMyProfessor and Reddit are user forums where people post their opinions. Multiple students can have different view and attitudes towards the same professor depending on their preferences, when they had the professor, and other factors.

2. Another possible issue is chunk boundaries. There may be important information that will be split across two chunks, especially with longer Reddit posts. If a query retrieves only one of those chunks, key context could be missing when a response is trying to be formed.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

+----------------------+
| Document Ingestion       |
| ------------------------ |
| Sources:                 |
| - Rate My Professor      |
| - Reddit Posts           |
| Tool: Python             |
| +----------+-----------+ |

       |
       v

+----------------------+
| Chunking                 |
| ------------------------ |
| Chunk Size: 300          |
| Overlap: 50              |
| Tool: Python             |
| +----------+-----------+ |

       |
       v

+----------------------+
| Embedding + Storage      |
| ------------------------ |
| ChromaDB                 |
| Model:                   |
| all-MiniLM-L6-v2         |
| Library:                 |
| sentence-transformers    |
| +----------+-----------+ |

       |
       v

+----------------------+
| Retrieval                |
| ------------------------ |
| Similarity Search        |
| Top-k = 5                |
| Library: ChromaDB        |
| +----------+-----------+ |

       |
       v

+----------------------+
| Generation               |
| ------------------------ |
| Retrieved Chunks +       |
| User Query               |
| LLM: Groq (llama-3.3-70b-versatile) |
| +----------------------+ |

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
