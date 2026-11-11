# Prompt Engineering

## 1. Introduction to Prompt Engineering

### What is Prompt Engineering?
Prompt engineering is the process of designing and improving instructions given to an AI model to get accurate, relevant, and useful responses.

### Why is Prompt Engineering Important?
A well-written prompt helps AI understand the task, follow instructions, reduce irrelevant answers, and produce better results.

### Discriminative AI
Discriminative AI learns patterns from data to classify or predict outcomes. For example, identifying whether an email is spam or not spam.

### Generative AI (GenAI)
Generative AI creates new content such as text, images, code, audio, and videos based on user instructions. Examples include ChatGPT and image-generation models.

### Discriminative AI vs Generative AI
- **Discriminative AI:** Focuses on distinguishing between categories or predicting labels.
- **Generative AI:** Focuses on generating new content based on learned patterns.

---

## 2. Context and Understanding in AI

### Long Context
Long context refers to an AI model's ability to process a large amount of input, such as lengthy documents, conversations, or code.

### Contextual Understanding
Contextual understanding means interpreting a prompt based on surrounding information rather than considering each word independently.

### Context Window
A context window is the maximum amount of information a model can process at one time, measured in tokens. It includes relevant input, conversation history, and generated output.

### Context Length
Context length refers to the number of tokens a model can handle within its context window. A larger context length allows the model to process more information.

### Contextual Understanding vs Context Window
- **Contextual understanding:** How well the model interprets the information.
- **Context window:** How much information the model can process at once.

### Few-Shot Learning
Few-shot learning is a technique where the model is given a small number of examples before being asked to perform a task. These examples help the model understand the expected pattern.

---

## 3. Types of Prompts

### Direct Prompting
Direct prompting means giving the AI a straightforward instruction without providing a detailed structure or multiple conditions.

**Example:**
```text
Explain what machine learning is.
```

### Structured Prompting
Structured prompting means organizing instructions into specific sections such as role, task, context, constraints, and output format.

**Example:**
```text
Role: You are a Python developer.

Task: Explain Python functions.

Context: The reader is a beginner.

Constraints: Use simple language and examples.

Output Format: Provide a definition, syntax, and example.
```

### Direct vs Structured Prompting
- **Direct prompting:** Simple instructions for straightforward tasks.
- **Structured prompting:** Detailed instructions for complex tasks requiring specific outputs.

---

## 4. Core Prompting Techniques

### Zero-Shot Prompting
Zero-shot prompting means asking an AI model to complete a task without providing examples. The model uses its existing training knowledge to understand the instruction.

**Example:**
```text
Classify this review as positive or negative:
"The product quality is excellent."
```

### Few-Shot Prompting
Few-shot prompting provides a few examples to demonstrate the expected input and output pattern.

**Example:**
```text
Text: I love this product.
Sentiment: Positive

Text: The service was terrible.
Sentiment: Negative

Text: The product is amazing.
Sentiment:
```

### Instruction Prompting
Instruction prompting involves giving the model clear and specific directions about what it should do.

**Example:**
```text
Summarize the following paragraph in exactly five bullet points.
Use simple English and do not add information that is not present.
```

### Zero-Shot vs Few-Shot Prompting
- **Zero-shot:** No examples are provided.
- **Few-shot:** A small number of examples are provided to guide the model.

---

## 5. Advanced Prompt Engineering Techniques

### ReAct Framework (Reasoning and Acting)
ReAct combines reasoning with actions. The AI determines what information or action is needed, uses an available tool, observes the result, and continues toward an answer.

**Basic flow:**

1. Reason: Determine what needs to be done.
2. Act: Use a tool, such as a search engine or API.
3. Observe: Examine the tool's result.
4. Continue: Use the observation to decide the next step.

**Example:** An AI assistant searches for information, reads the results, and uses them to answer a question.

### Tree of Thoughts (ToT)
Tree of Thoughts is a problem-solving approach where an AI explores multiple possible reasoning paths instead of following only one path.

**Example:** When solving a complex problem, the AI considers different approaches, evaluates them, and selects a suitable path.

### Directional Stimulus Prompting
Directional stimulus prompting provides additional hints or guidance to influence the model toward a particular type of response without specifying every detail.

**Example:**
```text
Explain climate change.
Focus on its causes, environmental impact, and possible solutions.
```

### Iterative Prompt Development
Iterative prompt development is the process of improving a prompt through repeated testing and refinement.

**Process:**
1. Write an initial prompt.
2. Generate an AI response.
3. Evaluate the response.
4. Identify missing details or errors.
5. Modify the prompt.
6. Test again until the desired output is achieved.

---

## 6. Prompt Engineering for Data and Automation Professionals

### Prompting for Data Professionals
Prompt engineering helps data professionals extract, organize, analyze, summarize, and interpret information using AI models.

**Example tasks:**
- Extracting information from documents.
- Cleaning and categorizing data.
- Converting unstructured information into structured data.
- Generating SQL queries.
- Summarizing reports.

### Data Extraction
Data extraction is the process of identifying and collecting specific information from a source such as a PDF, email, document, or webpage.

**Example:** Extracting candidate names, email addresses, phone numbers, and skills from resumes.

### Unstructured Data to Structured Data
Unstructured data does not follow a predefined format, whereas structured data is organized into a consistent format such as a table or JSON.

**Example:**

Unstructured input:
```text
John is a Python developer with 3 years of experience.
His email is john@example.com.
```

Structured output:
```json
{
  "name": "John",
  "role": "Python Developer",
  "experience": "3 years",
  "email": "john@example.com"
}
```

### Prompting for Automation
Prompting can help automate repetitive tasks such as extracting information, classifying documents, generating reports, and preparing structured outputs.

**Example:** Reading incoming emails, identifying their category, and extracting important details into JSON.

---

## 7. Prompt Engineering for Coding

### Prompting for Coding
Coding prompts provide instructions to AI models to generate, explain, debug, optimize, or review programming code.

### AI as a Developer's Assistant
AI can support developers throughout the software development process by helping with:

- **Code Generation:** Writing code based on requirements.
- **Code Explanation:** Explaining existing code line by line.
- **Debugging:** Identifying errors and suggesting fixes.
- **Code Optimization:** Improving performance and readability.
- **Code Review:** Identifying potential bugs and bad practices.
- **Documentation:** Generating comments and technical documentation.
- **Testing:** Creating test cases and explaining test failures.

### Effective Coding Prompt Structure
A good coding prompt should include:

1. **Role:** Define the AI's role, such as Python developer.
2. **Task:** Clearly describe what needs to be implemented.
3. **Context:** Provide existing code, project structure, or requirements.
4. **Constraints:** Mention programming language, libraries, and restrictions.
5. **Output Format:** Specify whether you need code, explanation, tests, or documentation.

**Example:**
```text
Role: You are an experienced Python developer.

Task: Create a function to validate email addresses.

Context: This function will be used in a FastAPI application.

Constraints:
- Use Python.
- Handle invalid input.
- Keep the code simple and reusable.

Output:
- Provide the complete function.
- Explain the code line by line.
- Include three test cases.
```

---

## 8. Important Concepts to Remember

| Concept | Main Purpose |
|---|---|
| Prompt Engineering | Designing effective AI instructions |
| Discriminative AI | Classification and prediction |
| Generative AI | Creating new content |
| Context Window | Maximum information processed at once |
| Contextual Understanding | Understanding information in context |
| Zero-Shot Prompting | Performing tasks without examples |
| Few-Shot Prompting | Learning task patterns from examples |
| Instruction Prompting | Following clear task instructions |
| ReAct | Combining reasoning and tool actions |
| Tree of Thoughts | Exploring multiple problem-solving paths |
| Directional Stimulus | Guiding the model toward a desired response |
| Iterative Development | Improving prompts through repeated testing |
| Data Extraction | Collecting specific information |
| Structured Output | Organizing information into a defined format |

---

## 9. Practical Applications of Prompt Engineering

- Building AI chatbots and virtual assistants.
- Extracting information from PDFs and resumes.
- Converting unstructured documents into JSON.
- Generating SQL queries and Python code.
- Automating repetitive business tasks.
- Summarizing lengthy documents.
- Analyzing customer feedback.
- Building RAG-based applications.
- Supporting software development and debugging.

---

## 10. Key Takeaways

1. Prompt engineering improves communication between users and AI models.
2. Clear instructions and relevant context improve output quality.
3. Zero-shot and few-shot prompting are fundamental prompting techniques.
4. Advanced techniques help with complex problem-solving and tool usage.
5. Structured prompts are useful when outputs must follow a specific format.
6. Prompt engineering is valuable in data extraction, automation, and software development.
7. AI-generated outputs should always be checked for accuracy and reliability.