# Retrieval-Augmented Generation (RAG)

## 1. What is RAG?
Retrieval-Augmented Generation (RAG) is an AI technique that combines information retrieval with Large Language Models (LLMs).  
It retrieves relevant information from external documents and uses that information to generate accurate, context-based answers.

## 2. Foundations of RAG
RAG is built on three main components: document retrieval, context preparation, and answer generation.  
It allows LLMs to use external knowledge instead of depending only on information learned during training.

## 3. Why is RAG Important?
LLMs may produce outdated or incorrect information because their knowledge comes from training data.  
RAG provides relevant external information to help generate more accurate and up-to-date responses.

## 4. Benefits of RAG
- **Updated Knowledge:** Uses external documents without retraining the entire model.
- **Reduced Hallucinations:** Grounds answers in retrieved information.
- **Cost Efficient:** Avoids expensive model retraining whenever documents change.
- **Source References:** Can provide references to the documents used for answering.
- **Domain-Specific Answers:** Supports applications using private or specialized business information.

## 5. RAG vs Semantic Search
Semantic search finds documents based on the meaning and intent of a user's query rather than exact keyword matches.  
RAG goes one step further by passing the retrieved information to an LLM to generate a natural-language answer.

## 6. Top-K Similar Chunks
Top-K retrieval selects the K most relevant document chunks based on their similarity to the user's query.  
For example, Top-5 retrieval returns the five most similar chunks for the LLM to use as context.

## 7. Key Technologies of RAG
- **Document Loaders:** Extract information from different document formats.
- **Text Splitters:** Divide documents into smaller chunks.
- **Embeddings:** Convert text into numerical vectors.
- **Vector Databases:** Store and search vector representations.
- **Retrievers:** Find relevant document chunks.
- **LLMs:** Generate answers using retrieved context.
- **Rerankers:** Reorder retrieved results based on relevance.

## 8. Document Loaders
Document loaders are tools used to import and extract content from different file formats and external sources.  
They convert documents into a common format, usually containing text and metadata, for further processing.

## 9. Text Loader
TextLoader is used to load plain text files into a document format that can be processed by RAG pipelines.  
It extracts the text content and makes it available for splitting, embedding, and retrieval.

## 10. PyPDF Loader
PyPDFLoader is a LangChain document loader that extracts text from PDF files using the PyPDF library.  
It can load PDF content page by page and preserve page-related metadata.

## 11. Directory Loader
DirectoryLoader loads multiple documents from a specified folder instead of loading files individually.  
It can use different document loaders to process multiple file formats within the same directory.

## 12. WebBaseLoader
WebBaseLoader is used to extract text content from web pages using their URLs.  
It helps build RAG applications that retrieve information from websites and online documentation.

## 13. CSV Loader
CSVLoader loads comma-separated values (CSV) files and converts their rows into documents.  
It is useful for processing structured data such as customer records, product information, and business datasets.

## 14. Document Parsing
Document parsing is the process of extracting meaningful information from files such as PDFs, Word documents, and HTML pages.  
It helps identify text, tables, headings, images, and other elements that can be used in a RAG pipeline.

## 15. Docling
Docling is an open-source document processing tool that converts complex documents into structured representations.  
It supports document understanding, including tables, headings, reading order, and layout information.

## 16. PyPDF
PyPDF is a Python library used to read, extract, split, merge, and manipulate PDF documents.  
It is commonly used in document processing pipelines to extract text and metadata from PDF files.

## 17. PyMuPDF
PyMuPDF is a Python library used to extract text, images, tables, and other information from PDF documents.  
It provides detailed access to PDF page content and layout, making it useful for advanced document processing.

## 18. Text Splitting
Text splitting is the process of dividing large documents into smaller pieces before generating embeddings.  
It makes information easier to retrieve and helps the LLM process relevant portions of a document.

## 19. Chunking
Chunking is the process of breaking large documents into smaller units called chunks.  
Each chunk can be converted into an embedding and stored in a vector database for efficient retrieval.

## 20. Chunking Methods
Different chunking methods divide documents based on character count, sentences, paragraphs, document structure, or semantic meaning.  
The appropriate method depends on the document format, content structure, and retrieval requirements.

## 21. Chunk Overlap
Chunk overlap means repeating a small portion of text between consecutive chunks.  
It prevents important information from being lost when a sentence or idea is divided across two chunks.

## 22. Character-Based Chunking
Character-based chunking divides text into chunks according to a fixed number of characters.  
It is simple to implement but may split sentences or paragraphs in the middle of an important idea.

## 23. Semantic Meaning-Based Chunking
Semantic chunking divides documents based on changes in meaning rather than fixed character lengths.  
It uses semantic similarity between sentences to identify natural boundaries between different topics.

## 24. Context-Aware Chunking
Context-aware chunking creates chunks while considering the meaning and surrounding information of the document.  
It helps preserve relationships between different sections and prevents important information from becoming isolated.

## 25. Text-Structure-Based Chunking
Text-structure-based chunking divides documents using their natural organization, such as headings, paragraphs, and sections.  
It preserves the original document structure and helps retrieve complete and meaningful information.

## 26. Sentence Splitting Using NLTK
NLTK is a Python library that provides natural language processing tools, including sentence tokenization.  
Its sentence tokenizer divides text into individual sentences while preserving sentence boundaries.

## 27. Recursive Character Text Splitting
RecursiveCharacterTextSplitter divides text using a hierarchy of separators such as paragraphs, newlines, spaces, and characters.  
It attempts to preserve natural text boundaries while maintaining the specified chunk size and overlap.

## 28. Document Structure-Based Chunking
Document structure-based chunking uses elements such as titles, headings, tables, and paragraphs to create meaningful chunks.  
It is particularly useful for structured documents such as reports, proposals, and business documents.

## 29. Contextual Chunking with LLM
Contextual chunking uses an LLM to understand the surrounding document information before preparing individual chunks.  
The model can add relevant context to each chunk so that its meaning remains clear during retrieval.

## 30. Post-Processing Chunks with Chunk Expansion
Chunk expansion retrieves additional neighboring chunks when an initial chunk is selected as relevant.  
It provides the LLM with more surrounding information and helps preserve the complete meaning of the retrieved content.

## 31. Vector Database
A vector database stores numerical representations of text, images, and other data called embeddings.  
It enables similarity-based searches to identify information that is semantically related to a user's query.

## 32. Types of Vector Databases
- **ChromaDB:** An open-source vector database commonly used in RAG applications and experimentation.
- **FAISS:** A library developed by Meta for efficient similarity search and clustering of vectors.
- **Pinecone:** A managed vector database designed for scalable vector search.
- **Weaviate:** An open-source vector database supporting vector and hybrid search.
- **Milvus:** A vector database designed for large-scale vector storage and retrieval.
- **Qdrant:** A vector database supporting similarity search, metadata filtering, and payload storage.

## 33. Types of Vector Search
- **Exact Search (Brute Force):** Compares a query vector against every stored vector to find the closest matches.
- **Approximate Nearest Neighbor (ANN):** Uses optimized indexing techniques to find similar vectors faster without comparing every stored vector.
- **Hybrid Search:** Combines semantic vector search with keyword-based search to improve retrieval results.

## 34. Tool Calling
Tool calling allows an LLM to interact with external tools, functions, APIs, or databases to perform specific tasks.  
For example, an LLM can call a retrieval tool to search a vector database and obtain relevant documents before answering.

## 35. Retrieval Pipeline
A retrieval pipeline is the process of finding relevant information from stored documents based on a user's query.  
It typically includes query processing, embedding generation, similarity search, filtering, reranking, and context preparation.

## 36. Two Retrieval Methods
**1. Dense Retrieval:** Converts queries and documents into vector embeddings and retrieves information based on semantic similarity.  
**2. Sparse Retrieval:** Uses keyword-based techniques such as BM25 to find documents based on matching terms and their importance.

## 37. Top-K Retrieval
Top-K retrieval returns a fixed number of the most relevant document chunks for a given query.  
Choosing the correct K value helps balance information coverage, retrieval quality, and the LLM's context window.

## 38. Reranking
Reranking is the process of reorganizing retrieved documents according to their relevance to the user's query.  
It improves retrieval quality by moving the most useful chunks to the top before passing them to the LLM.

## 39. Cross-Encoder Reranker
A cross-encoder evaluates a query and document together to calculate how relevant the document is to that query.  
It generally provides more accurate relevance scores than simple embedding similarity but requires additional computation for each query-document pair.

## 40. Metadata Filtering
Metadata filtering uses additional information attached to documents to narrow down retrieval results.  
Metadata can include file names, document types, dates, page numbers, departments, and access permissions.

## 41. Two Types of Metadata Filtering
**1. Pre-Filtering:** Applies metadata conditions before or during the vector search to restrict the candidate documents.  
**2. Post-Filtering:** Applies metadata conditions after the initial retrieval to remove results that do not satisfy the conditions.

## 42. Access Control Filtering
Access control filtering ensures users can retrieve only the documents they are authorized to access.  
It uses permissions, user roles, and department information to prevent unauthorized access to private data.

## 43. Vector Database Indexes
Vector database indexes organize stored embeddings to make similarity searches faster and more efficient.  
Common indexing approaches include HNSW, IVF, and flat indexes, each offering different trade-offs between speed, accuracy, and memory usage.

## 44. Query Transformation Techniques
Query transformation modifies or expands a user's original question to improve retrieval results.  
Common techniques include query rewriting, query expansion, multi-query retrieval, and hypothetical document embeddings (HyDE).

## 45. Latency
Latency refers to the time taken by a RAG application to process a query and return an answer.  
It can be affected by embedding generation, vector search, reranking, LLM generation, and network communication.

## 46. Common Retrieval Failures and Fixes
- **Poor Chunking:** Use appropriate chunk sizes, overlap, and structure-aware splitting.
- **Missing Information:** Improve document parsing and ensure all relevant content is extracted.
- **Incorrect Retrieval:** Use hybrid search, query rewriting, or reranking.
- **Too Much Context:** Adjust Top-K values and remove irrelevant chunks.
- **Missing Metadata:** Add useful metadata during document processing.
- **Unauthorized Retrieval:** Apply access control and metadata-based permission filters.

## 47. Corrective RAG (CRAG)
Corrective Retrieval-Augmented Generation (CRAG) is an approach that evaluates the quality of retrieved documents before generating an answer.  
If the retrieved information is insufficient or irrelevant, the system can trigger additional retrieval or web searches to improve the context.

## 48. RAG vs Fine-Tuning
RAG retrieves external information at query time and provides it to an LLM as additional context.  
Fine-tuning modifies the model's learned parameters using task-specific training data to adapt its behavior.

## 49. LoRA (Low-Rank Adaptation)
LoRA is a parameter-efficient fine-tuning technique that trains small additional matrices instead of updating all the original model parameters.  
It reduces training costs, memory requirements, and the number of parameters that need to be updated.

## 50. QLoRA (Quantized Low-Rank Adaptation)
QLoRA combines model quantization with LoRA to reduce the memory required for fine-tuning large language models.  
It loads the base model in a low-bit format, commonly 4-bit, while training small LoRA adapter weights.

## 51. LangChain
LangChain is an open-source framework used to build applications powered by large language models.  
It provides components for document loading, text splitting, embeddings, vector stores, retrievers, prompts, and LLM integration.

## 52. Complete RAG Workflow
1. **Document Loading:** Load documents from PDFs, CSV files, websites, and other sources.
2. **Document Parsing:** Extract text, tables, headings, and other relevant content.
3. **Text Splitting:** Divide the extracted content into smaller chunks.
4. **Embedding Generation:** Convert each chunk into a numerical vector.
5. **Vector Storage:** Store embeddings and associated metadata in a vector database.
6. **User Query:** Receive a question from the user.
7. **Query Processing:** Transform or embed the question for retrieval.
8. **Retrieval:** Find the most relevant document chunks using vector or hybrid search.
9. **Reranking:** Reorder retrieved chunks according to relevance.
10. **Context Preparation:** Pass the selected chunks and user question to the LLM.
11. **Answer Generation:** Generate a response based on the retrieved information.
12. **Evaluation:** Measure answer quality, retrieval accuracy, relevance, and faithfulness.

---

## Conclusion
RAG improves LLM applications by connecting language models with external and domain-specific knowledge sources.  
A well-designed RAG pipeline depends on effective document processing, chunking, embeddings, retrieval, reranking, and answer evaluation.