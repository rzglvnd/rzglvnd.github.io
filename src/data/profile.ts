export const siteMeta = {
  title: "Reza Ghalavand",
  role: "Applied AI Engineer",
  tagline: "LLM Systems · RAG · Agents · Evaluation · Python · AI Infrastructure",
  description:
    "Reza Ghalavand, Applied AI Engineer building Python LLM systems, RAG, and agent evaluation tools, backed by 15+ years of software engineering.",
  siteUrl: "https://rzglvnd.github.io",
  email: "rzglvnd@gmail.com",
  linkedin: "https://linkedin.com/in/rzglvnd",
  github: "https://github.com/rzglvnd",
  resumePath: "/assets/resume/Reza_Ghalavand_Resume_2026.pdf"
};

export const professionalSummary =
  "Applied AI Engineer building LLM applications, retrieval pipelines, and agent governance tools in Python. I bring 15+ years of software, backend, and database experience to making AI systems testable, maintainable, and ready for operational scrutiny.";

export const competencies = [
  { category: "Applied AI", items: ["LLMs", "RAG", "Agent governance", "LangGraph", "LangChain", "Prompt Engineering", "Policy evaluation"] },
  { category: "AI and Backend Engineering", items: ["Python", "FastAPI", "REST APIs", "pytest", "Backend architecture"] },
  { category: "Data and Retrieval", items: ["Embeddings", "FAISS", "TF-IDF", "SQL Server", "PostgreSQL", "Redis"] },
  { category: "Infrastructure and Delivery", items: ["Docker", "Git", "GitHub Actions", "Linux", "Kubernetes"] },
  { category: "Software Engineering Foundation", items: [".NET", "C#", "C++", "PHP", "Enterprise systems"] }
] as const;

export const experience = [
  {
    title: "Senior IT Systems Engineer",
    company: "Esfahan Regional Electric Company",
    period: "2025-Present",
    highlights: [
      "Support enterprise IT systems, backend infrastructure, automation initiatives, and mission-critical software operations."
    ]
  },
  {
    title: "Senior Software Programmer",
    company: "Yeganeh Computer Center",
    period: "2010-2025",
    highlights: [
      "Developed enterprise backend features.",
      "Optimized SQL Server performance and modernized legacy codebases.",
      "Created technical documentation and automated business processes using Python."
    ]
  },
  {
    title: "Remote Technical Support, DBA and AI Automation Developer",
    company: "Darya System (Remote)",
    period: "2022-Present",
    highlights: [
      "Provided ERP support and administered SQL Server environments.",
      "Built Python automation tools and improved reporting and operational workflows."
    ]
  }
] as const;

export const selectedProjects = [
  {
    name: "Local LLM Chat Engine",
    caseStudyHref: "/projects/?project=engine",
    href: "https://github.com/rzglvnd/local-llm-chat-engine",
    summary: "Modular Python RAG backend with ingestion, optional embeddings/FAISS retrieval, TF-IDF snapshots, API/CLI access, and local or hosted model adapters.",
    stack: ["FastAPI", "RAG", "Python"]
  },
  {
    name: "LangGraph Governance Lab",
    caseStudyHref: "/projects/?project=governance",
    href: "https://github.com/rzglvnd/langgraph-governance-lab",
    summary: "FastAPI service evaluating agent traces against tool, approval, model, and budget policies. Deterministic findings with optional LLM remediation advice.",
    stack: ["Python", "FastAPI", "Policy evaluation"]
  },
  {
    name: "AI Systems Notes",
    caseStudyHref: "/projects/?project=notes",
    href: "https://github.com/rzglvnd/ai-systems-notes",
    summary: "Versioned engineering handbook covering LLM architecture, retrieval, evaluation, security, and operations. Reference patterns are distinguished from runtime implementations.",
    stack: ["MkDocs", "Python", "AI Systems"]
  },
  {
    name: "ERP AI Assistant",
    href: "https://github.com/rzglvnd/erp-ai-assistant",
    summary: "Enterprise-oriented workflow assistant for ERP-related automation.",
    stack: ["FastAPI", "ERP", "LLM Integration"]
  },
  {
    name: "Telecom Analytics Lab",
    href: "https://github.com/rzglvnd/telecom-analytics-lab",
    summary: "Analytics workflows and APIs for telecom operations datasets.",
    stack: ["Python", "Analytics", "Operations"]
  },
  {
    name: "System Design Notes",
    href: "https://github.com/rzglvnd/system-design-notes",
    summary: "System design and architecture handbook with practical guidance.",
    stack: ["Architecture", "Documentation", "Engineering"]
  }
] as const;

export const education = {
  degree: "B.Sc. Software Engineering",
  institution: "Islamic Azad University of Najafabad"
};

export const focusAreas = [
  "LLM services with explicit operational boundaries",
  "Agent governance, safety controls, and evaluation workflows",
  "LLM and RAG integration patterns for backend systems",
  "Reliable APIs, observability, and operational excellence"
] as const;
