const base = 'https://github.com/rzglvnd/';
export const skills = ['RAG', 'Agents', 'Evaluation', 'Backend', 'Ops'];
export const projects = [
  {
    id: 'notes', number: '01', name: 'AI Systems Notes', short: 'AI Systems Notes',
    kind: 'ENGINEERING HANDBOOK', state: 'Core handbook complete', cardState: 'Living handbook',
    summary: 'An engineering playbook for the decisions around LLMs: retrieval, evaluation, security, and operating the system.',
    problem: 'AI knowledge is scattered across tools and demos. Teams need a coherent set of patterns for designing, evaluating, and operating an LLM system.',
    solution: 'Organizes practical engineering knowledge into a versioned handbook, with reference architecture layers, runnable examples, and a repeatable documentation build.',
    technologies: ['Python', 'MkDocs', 'Markdown', 'GitHub Actions'],
    stack: 'MkDocs · Python · GitHub Actions',
    tags: ['RAG', 'Agents', 'Evaluation', 'Ops'],
    repo: base + 'ai-systems-notes',
    current: 'The roadmap marks the v0.1 core handbook complete. Reproducible benchmarks and deployment recipes are in progress; reference local LLM implementations remain a later milestone.',
    implemented: ['Architecture, retrieval, evaluation, security, and operations chapters', 'MkDocs site with a lightweight Python viewer', 'Documentation build validation in GitHub Actions'],
    tradeoff: 'A documentation-first project: its architecture diagrams describe reference patterns. They are not evidence of a deployed runtime or benchmark results.',
    strengths: 'Technical writing, architecture communication, and translating AI concepts into engineering decisions.',
    architectureLabel: 'REFERENCE ARCHITECTURE',
    architectureNote: 'Reference layers from the handbook. Safety/governance and the platform span the entire flow.',
    nodes: [
      ['Experience', 'Chat UI, API clients, and automation triggers are the entry points into an AI system.'],
      ['API orchestration', 'Validate requests, apply authentication and limits, and route work to the appropriate model or service.'],
      ['Retrieval', 'Index content, choose chunking and metadata strategies, and retrieve context independently of generation.'],
      ['Generation', 'Isolate model providers behind adapters; consider fallback behavior and streaming responses.']
    ],
    evidence: {
      RAG: ['documented', 'Documented', 'Retrieval, embeddings, vector stores, and architecture patterns.'],
      Agents: ['documented', 'Documented', 'LangGraph and agentic AI are part of the handbook’s stated scope.'],
      Evaluation: ['documented', 'Documented', 'Evaluation guidance; reproducible benchmark suite in progress.'],
      Backend: ['documented', 'Documented', 'Reference API orchestration and model adapter boundaries.'],
      Ops: ['documented', 'Documented + CI', 'Operations/deployment guidance and a validated docs build.']
    },
    links: [['Readme', ''], ['Architecture', '/blob/main/docs/architecture.md'], ['Roadmap', '/blob/main/docs/roadmap.md']]
  },
  {
    id: 'governance', number: '02', name: 'LangGraph Governance Lab', short: 'Governance Lab',
    kind: 'AGENT GOVERNANCE', state: 'Evaluation service implemented', cardState: 'Working service',
    summary: 'A policy evaluation service that makes agent runs inspectable through deterministic checks and actionable findings.',
    problem: 'Agent runs can exceed budgets, use restricted tools, or miss required approvals. Their behavior needs explicit checks and findings that can be traced to individual steps.',
    solution: 'Accepts policies and submitted run traces through a FastAPI service. Deterministic rules evaluate tool use, approvals, model allow-lists, step limits, and cost caps; optional LLM advice helps explain remediation.',
    technologies: ['Python', 'FastAPI', 'Uvicorn', 'Requests', 'pytest', 'Docker'],
    stack: 'Python · FastAPI · pytest · Docker',
    tags: ['Agents', 'Evaluation', 'Backend', 'Ops'],
    repo: base + 'langgraph-governance-lab',
    current: 'Policy validation, individual and batch run evaluation, and optional LLM remediation advice are implemented. The repository includes tests, CI, Docker packaging, and operational documentation.',
    implemented: ['Deterministic checks with step-level violation codes', 'Optional API key protection and configurable rate limits', 'Liveness/readiness endpoints and request IDs'],
    tradeoff: 'Evaluates submitted traces; it does not itself stop tools during execution. LangGraph is the target workflow context, not a required runtime dependency. Production enforcement needs integration with the executing workflow.',
    strengths: 'Agent governance, deterministic evaluation, clear API contracts, and separating policy decisions from generative advice.',
    architectureLabel: 'EVALUATION SERVICE',
    architectureNote: 'Optional LLM remediation follows evaluation and does not determine the policy result.',
    nodes: [
      ['Run + policy', 'The client submits a policy and an agent run trace, including tool/model metadata and any recorded approvals.'],
      ['API validation', 'server.py validates and orchestrates policy validation and single or batch evaluation requests.'],
      ['Rule engine', 'governance.py checks tools, approvals, models, step counts, and total cost deterministically.'],
      ['Findings + advice', 'Return violations and rule-based recommendations. An optional upstream LLM can add remediation advice.']
    ],
    evidence: {
      RAG: ['none', 'Not a core focus', 'No retrieval pipeline demonstrated by this project.'],
      Agents: ['implemented', 'Implemented', 'Run-trace policies for tools, human approvals, models, and budgets.'],
      Evaluation: ['implemented', 'Implemented', 'Deterministic governance checks and batch run evaluation.'],
      Backend: ['implemented', 'Implemented', 'FastAPI policy/evaluation endpoints with bounded inputs.'],
      Ops: ['implemented', 'Implemented', 'Health checks, optional auth/rate limits, Docker, tests, and CI.']
    },
    links: [['Readme', ''], ['Design', '/blob/main/docs/design.md'], ['Rule engine', '/blob/main/governance.py'], ['Evaluation', '/blob/main/docs/evaluation.md']]
  },
  {
    id: 'engine', number: '03', name: 'Local LLM Chat Engine', short: 'Local LLM Engine',
    kind: 'RETRIEVAL & GENERATION', state: 'API and CLI implemented', cardState: 'Working service',
    summary: 'A modular chat backend that connects document retrieval to interchangeable model adapters, with API and CLI access.',
    problem: 'Local AI experiments often couple the model, retrieval, and API. That makes it harder to change backends, reproduce state, or run without heavy optional dependencies.',
    solution: 'Separates retrieval from generation. A TF-IDF baseline works without dense-retrieval packages, optional embeddings/FAISS extend search, and adapters connect retrieved context to local or hosted models.',
    technologies: ['Python', 'FastAPI', 'scikit-learn', 'sentence-transformers', 'FAISS', 'Hugging Face', 'OpenAI', 'pytest', 'Docker'],
    stack: 'FastAPI · TF-IDF · FAISS · Model adapters',
    tags: ['RAG', 'Backend', 'Ops'],
    repo: base + 'local-llm-chat-engine',
    current: 'The repository provides ingestion, search, chat, and streaming endpoints; CLI commands; TF-IDF snapshots; and echo, OpenAI, and Hugging Face adapters. Dense retrieval is optional.',
    implemented: ['Swappable TF-IDF, embedding, and FAISS retrieval paths', 'Snapshot save/load and startup autoload', 'API/CLI interfaces, Docker packaging, tests, and CI'],
    tradeoff: 'OpenAI supports native token streaming; local Hugging Face output is chunked after generation. “Local” describes a supported deployment path; choosing the OpenAI adapter uses a hosted provider.',
    strengths: 'RAG integration, modular Python backend engineering, graceful dependency fallbacks, and operational configuration.',
    architectureLabel: 'RETRIEVAL-AUGMENTED CHAT',
    architectureNote: 'Ingestion indexes documents before queries. TF-IDF is the baseline; dense retrieval is optional.',
    nodes: [
      ['API / CLI', 'Ingest normalized documents or query the service through FastAPI endpoints and command-line utilities.'],
      ['Retrieval store', 'Search TF-IDF or optional embedding/FAISS backends for relevant context. TF-IDF snapshots preserve retrieval state.'],
      ['Model adapter', 'Attach retrieved context and route the chat request to echo, OpenAI, or a local Hugging Face generation pipeline.'],
      ['Chat / SSE', 'Return a response or emit incremental SSE chunks. Actual token streaming depends on the selected model backend.']
    ],
    evidence: {
      RAG: ['implemented', 'Implemented', 'Ingestion, retrieval, context attachment, and model adapters.'],
      Agents: ['none', 'Not a core focus', 'A retrieval/chat backend; no agent execution loop claimed.'],
      Evaluation: ['documented', 'Tests included', 'Repository tests and CI; no answer-quality benchmark claimed.'],
      Backend: ['implemented', 'Implemented', 'API, CLI, streaming, adapter boundaries, and snapshots.'],
      Ops: ['implemented', 'Implemented', 'Health checks, environment config, auth/rate limits, Docker, and CI.']
    },
    links: [['Readme', ''], ['Architecture', '/blob/main/docs/architecture.md'], ['Adapters & streaming', '/blob/main/docs/adapters.md'], ['Operations', '/blob/main/docs/operations.md']]
  }
];

// Present executable application evidence before the supporting handbook.
projects.sort((a, b) => ['engine', 'governance', 'notes'].indexOf(a.id) - ['engine', 'governance', 'notes'].indexOf(b.id));
