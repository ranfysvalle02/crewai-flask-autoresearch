# AI Research Assistant
![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/90b64e83-4302-4b6d-9f79-63c40851dc3b/image.png?t=1717410721)

## The Unpredictable Mind of AI Agents

One of the most significant challenges in LLM-powered agents is the unpredictability of their planning processes. While these agents can generate impressive outputs, their internal reasoning is often opaque, making it difficult to understand how they arrived at their conclusions. This lack of transparency makes it challenging to understand and control the agent's behavior.

### The Black Box of AI Reasoning
* **Complex Internal Mechanisms:** LLMs are incredibly complex systems with billions of parameters. Their reasoning process involves intricate interactions between these parameters, making it difficult to trace the exact steps that led to a given output.
* **Data-Driven Nature:** LLMs are trained on massive datasets, and their responses are influenced by the patterns and correlations they have learned from this data. This can make it challenging to predict how they will respond to new or unusual prompts.
* **Randomness:** LLMs often incorporate elements of randomness into their decision-making processes. This can introduce variability into their outputs, even for the same prompt.

### The Implications of Uncontrolled Behavior
This unpredictability can have significant implications for the use of LLM-powered automations. It can make it difficult to:
* **Debug Errors:** When an agent produces an incorrect or unexpected result, it can be challenging to determine the root cause.
* **Ensure Reliability:** It can be difficult to guarantee that an agent will consistently produce accurate and reliable outputs.
* **Understand Limitations:** It can be challenging to identify the limitations of an agent and determine when it is not suitable for a particular task.

### Addressing the Challenge
While it may not be possible to completely eliminate the unpredictability of LLM-powered agents, there are steps that can be taken to mitigate its effects. These include:
* **Rigorous Testing:** Thoroughly testing agents in a variety of scenarios can help to identify potential issues and improve their reliability.
* **Human Oversight:** Incorporating human oversight can help to ensure that agents are used appropriately and that their outputs are reviewed for accuracy.
* **Transparency Efforts:** Researchers are actively working on developing techniques to make the reasoning processes of LLMs more transparent.

## Beyond the Hype: Understanding the Limitations of LLMs

**The Challenge of Control**

One of the most significant hurdles in harnessing the power of LLMs is their propensity to generate unexpected or even harmful outputs. This can occur due to various factors, including:

* **Bias in Training Data:** If the data used to train an LLM is biased, the model will inevitably reflect those biases in its responses.
* **Prompt Engineering:** The specific wording of a prompt can significantly influence the output, making it difficult to predict how a model will respond to certain queries.
* **Emergent Behaviors:** As LLMs become more complex, they can exhibit unexpected behaviors that are difficult to explain or control.

**LLMs as Mathematical Models**

It's essential to understand that LLMs are fundamentally mathematical models. They are designed to process and generate text based on patterns and correlations found in massive datasets. While they can produce impressive results, their "intelligence" is not the same as human intelligence.

* **Lack of Understanding:** LLMs do not truly understand the meaning of the words they generate. They simply manipulate symbols based on statistical probabilities.
* **Dependence on Training Data:** The quality and quantity of the training data are crucial factors in determining an LLM's performance. A model trained on limited or biased data will have limitations.

## Potential Problems for an LLM Filling Out a Template with Color-Coded Ratings

An LLM (Large Language Model) can encounter several challenges when filling out a template with color-coded ratings (🔴, 🟡, 🟢). These challenges arise due to the nuances of natural language understanding, knowledge representation, and task-specific requirements.

### 1. **Subjectivity and Contextual Understanding:**
* **Ambiguity in Ratings:** The terms "High," "Medium," and "Low" can be subjective and depend on the context. For example, a "High" risk for a small business might be a "Low" risk for a multinational corporation.
* **Contextual Nuances:** The LLM might struggle to understand the specific context of the template and the implications of different ratings. For instance, a "High" rating for a safety feature might have a different impact than a "High" rating for a marketing campaign.

### 2. **Knowledge Gaps and Inconsistency:**
* **Lack of Domain Expertise:** If the LLM lacks sufficient domain knowledge, it might assign incorrect ratings. For example, a model might rate the complexity of a medical procedure as "Low" if it doesn't understand the underlying medical concepts.
* **Inconsistent Ratings:** The LLM might provide inconsistent ratings for similar items or situations, leading to errors and inconsistencies in the filled-out template.

### 3. **Template Structure and Complexity:**
* **Complex Templates:** If the template is highly complex with multiple interconnected fields, the LLM might struggle to understand the relationships between different elements and assign appropriate ratings.
* **Ambiguous Instructions:** If the instructions for filling out the template are unclear or ambiguous, the LLM might misinterpret them and provide incorrect ratings.

### 4. **Data Quality and Bias:**
* **Biased Training Data:** If the LLM was trained on biased data, it might perpetuate those biases in its ratings, leading to unfair or inaccurate assessments.
* **Data Limitations:** If the LLM doesn't have access to sufficient or relevant data, it might struggle to provide accurate ratings.

## **Expanding on LLM Bias and Explainability Techniques**

### **Understanding LLM Bias**

* **Types of Bias:**
  * **Representation Bias:** When the training data doesn't represent the diversity of the real world.
  * **Association Bias:** When the model associates certain attributes with negative or positive outcomes.
  * **Confirmation Bias:** When the model reinforces existing beliefs or stereotypes.

* **Impact:**
  * **Reinforcing harmful stereotypes**
  * **Discriminating against certain groups**
  * **Eroding trust in AI systems**

### **Explainability Techniques for LLMs**

* **Attention Visualization:** Visualize the attention weights assigned to different parts of the input, revealing which parts of the text are most influential in the model's output.
* **Saliency Maps:** Highlight the most important regions of an input image or text that contribute to the model's prediction.
* **Counterfactual Explanations:** Generate alternative inputs that would have led to different outputs, helping to understand the model's decision boundaries.
* **SHAP (SHapley Additive exPlanations):** Attribute the contribution of each feature to the model's prediction.

**The Proprietary Challenge: Limitations in Directly Applying Explainability Techniques to OpenAI Models**

While the explainability techniques discussed earlier provide valuable insights into LLM decision-making, their direct application to OpenAI models can be challenging due to proprietary nature of these models. 

Here are some key limitations:

* **Black Box Architecture:** OpenAI models are often designed as black boxes, meaning the internal workings and parameters are not publicly accessible. This makes it difficult to directly apply techniques that require detailed knowledge of the model's architecture, such as attention visualization or saliency maps.
* **Limited Access to Training Data:** The training data used to develop OpenAI models is proprietary, making it impossible to analyze the data directly for biases or other issues. This limits the effectiveness of techniques that rely on understanding the composition of the training data.
* **API Constraints:** When using OpenAI models through an API, access to the underlying model may be restricted. This can prevent the application of techniques that require direct interaction with the model's internals.

**Workarounds:**

* **Proxy Models:** Creating proxy models that mimic the behavior of large language models can provide insights into their decision-making processes. While not perfect, these proxy models can be used to apply explainability techniques.
* **Adversarial Attacks:** Adversarial attacks can be used to probe the model's vulnerabilities and identify potential biases. By understanding how the model reacts to carefully crafted inputs, we can gain insights into its decision-making process.

While the challenges of understanding and controlling LLM bias are significant, it's precisely this element of unpredictability that makes these models so fascinating. The enigmatic nature of their decision-making processes, coupled with their immense potential, invites us to explore the boundaries of AI and to strive for a future where LLMs are both powerful and responsible tools.

## Getting Started
This is a Flask application that uses Azure OpenAI to perform research on a company and generate a report on its potential for partnership opportunities. The application uses the DuckDuckGo search engine to gather information about the company and then uses Azure OpenAI to analyze the data and generate a report. The report includes information on the company's reputation, financial stability, compliance, strategic goals, and innovation.

Let's begin!

1. Clone the repository.
2. Install the required packages using pip


## Configuration

The application requires the following environment variables:

- `OPENAI_AZURE_ENDPOINT`: The endpoint for the Azure OpenAI API.
- `OPENAI_AZURE_API_KEY`: The API key for the Azure OpenAI API.

## Crew Code

```python
class CustomCrew:
    def __init__(self, company_name):
        self.company_name = company_name

    def run(self):
       # Define agent with a more specific role and backstory
        custom_agent_1 = Agent(
            role="Partner Compatibility Analyst",
            backstory="I am an expert in assessing the suitability of potential business partners. I have a deep understanding of industry trends, financial analysis, and partnership dynamics.",
            goal=f"Using the snippets provided from your web search tool, generate an HTML report on {self.company_name} for potential partnership opportunities with {target}, focusing on financial stability, industry reputation, and alignment with strategic goals.",
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=default_llm,
            memory=True, # Enable memory
            max_iter=50, # Default value for maximum iterations
        )
        custom_task_1 = Task(
            description=dedent(
                f"""
                Perform a 3-5 web searches using your web search tool to analyze {self.company_name}:                
                    Use your tools and provide a recommendation on partner compatibility.
                    Answer to the best of your ability.
                    IMPORTANT! Your output should follow the provided template.
                    Be concise in your recommendation.
                    MAX RESPONSE LENGTH IS 500 CHARACTERS.
                    IMPORTANT! PERFORM AT LEAST 3-5 WEB SEARCHES.
                    MAX. 5 WEB SEARCHES.
                    CREATE AN HTML STRING USING THE PROVIDED TEMPLATE! IMPORTANT!
                    THINK CRITICALLY AND STEP BY STEP!

            """+"\n\n[additional context]"+target_context+"\n\n[end additional context]"
            ),
            agent=custom_agent_1,
            expected_output=""" <expected-output> """,
        )


        # Define crew with updated agents and tasks
        crew = Crew(
            agents=[custom_agent_1],
            tasks=[custom_task_1],
            verbose=True,
        )

        # Run the crew and format output for HTML
        result = crew.kickoff()

        # Extract relevant information from CrewAI output (modify as needed)
        html_output = result  # Assuming findings are in the first agent's output

        return html_output


@app.route('/demo', methods=['GET', 'POST'])
def test_endpoint():
    user_input = ''
    ai_response = ''
    if request.method == 'POST':
        if 'reset' in request.form:
            session['reset'] = True
            return redirect(url_for('test_endpoint'))
        else:
            user_input = request.form.get('user-input')
            custom_crew = CustomCrew(user_input)
            result = custom_crew.run()
            
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:8080/demo`.
3. Enter the name of the company you want to research and click "Start Research".
4. The application will perform the research and display the report in the browser.

