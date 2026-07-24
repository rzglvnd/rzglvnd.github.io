export const siteMeta = {
  title: "Reza Ghalavand",
  role: "Senior Software Engineer",
  tagline: "Backend and Enterprise Systems | AI Applications",
  description:
    "Personal website of Reza Ghalavand focused on enterprise backend engineering, practical AI systems, and technical writing.",
  siteUrl: "https://rzglvnd.github.io",
  email: "rzglvnd@gmail.com",
  linkedin: "https://linkedin.com/in/rzglvnd",
  github: "https://github.com/rzglvnd",
  resumePath: "/assets/resume/Reza_Ghalavand_Resume_2026.pdf"
};

export const professionalSummary =
  "Senior Software Engineer with 15+ years of experience delivering enterprise software, backend systems, ERP solutions, and SQL Server administration. Experienced in designing maintainable systems, modernizing legacy applications, and automating operational workflows. Currently focused on applying Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), LangGraph, and Python to build practical AI-powered software for enterprise environments.";

export const competencies = [
  {
    category: "Languages",
    items: ["Python", "C#", "C++", "PHP"]
  },
  {
    category: "Backend",
    items: [".NET", "FastAPI", "REST APIs"]
  },
  {
    category: "Databases",
    items: ["SQL Server", "PostgreSQL", "Redis"]
  },
  {
    category: "AI",
    items: ["LLMs", "RAG", "LangGraph", "LangChain", "Prompt Engineering"]
  },
  {
    category: "Infrastructure",
    items: ["Docker", "Git", "Linux", "Kubernetes"]
  },
  {
    category: "Domains",
    items: ["Enterprise Software", "ERP", "Database Administration"]
  }
] as const;

export const experience = [
  {
    title: "Senior IT Systems Engineer",
    company: "Esfahan Regional Electric Company",
    period: "Current",
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
    name: "AI Systems Notes",
    href: "https://github.com/rzglvnd/ai-systems-notes",
    summary: "Open-source knowledge base for practical AI engineering.",
    stack: ["MkDocs", "Python", "AI Systems"]
  },
  {
    name: "LangGraph Governance Lab",
    href: "https://github.com/rzglvnd/langgraph-governance-lab",
    summary: "Research repository exploring governance and orchestration patterns.",
    stack: ["FastAPI", "LangGraph", "Governance"]
  },
  {
    name: "Local LLM Chat Engine",
    href: "https://github.com/rzglvnd/local-llm-chat-engine",
    summary: "Production-oriented local LLM platform with modular architecture.",
    stack: ["FastAPI", "RAG", "Python"]
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
  "Production-ready AI services for enterprise use cases",
  "Agent governance, safety controls, and evaluation workflows",
  "LLM and RAG integration patterns for backend systems",
  "Reliable APIs, observability, and operational excellence"
] as const;
