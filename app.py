import json
from textwrap import dedent
from flask import Flask, request, render_template_string, session, redirect, url_for
import os
from langchain_openai import AzureChatOpenAI
from crewai import Crew, Task, Agent
from crewai_tools import BaseTool
from duckduckgo_search import DDGS
from youtube_transcript_api import YouTubeTranscriptApi
# Azure OpenAI configuration
azure_openai_endpoint = os.getenv('OPENAI_AZURE_ENDPOINT', "")
azure_openai_api_key = os.getenv('OPENAI_AZURE_API_KEY', '')
azure_openai_deployment_id = 'gpt-35-turbo'

default_llm = AzureChatOpenAI(
    openai_api_version="2023-07-01-preview",
    azure_deployment=azure_openai_deployment_id,
    azure_endpoint=azure_openai_endpoint,
    api_key=azure_openai_api_key,
    model_name="gpt-3.5-turbo"
)
def extract_youtube_id_from_href(href_url):
    # Split the URL on the '=' character
    url_parts = href_url.split('=')
    # The video ID is the part after 'v', which is the last part of the URL
    video_id = url_parts[-1]
    return video_id
def get_transcript(video_id):
  """Fetches the transcript for a given YouTube video ID.
  Args:
    video_id: The ID of the YouTube video.
  Returns:
    A list of transcript segments, or None if no transcript is found.
  """

  try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    alltext = (' '.join(item['text'] for item in transcript))
    return alltext
  except Exception as e:
    print(f"Error fetching transcript for {video_id}: {e}")
    return None
class WebSearch(BaseTool):
    name: str = "Web Search"  # Add type annotation for 'name'
    description: str = "Searches the web for relevant content."
    def _run(self, query: str) -> str:
        query = query + " 2024 company video site:youtube.com AND inlang:en AND inurl:youtube AND inurl:v="
        results = DDGS().text(str(query),region="us-en", max_results=1)
        VIDEO_IDS = []
        video_transcript_text = ""
        for result in results:
            VIDEO_IDS.append(result["href"])
            video_transcript_text = get_transcript(extract_youtube_id_from_href(result["href"]))
        print(VIDEO_IDS)
        messages = [
            (
                "system",
                "You are a helpful assistant that summarizes video transcripts into detailed markdown with key facts in list format.",
            ),
            ("human", "What are some key facts about the following content:\n\n" + video_transcript_text),
            ("human", f"""
             [response format]
                - MUST BE VALID MARKDOWN LIST FORMAT
                - MUST BE VALID MARKDOWN STRING
             [end response format]

             FOCUS ON {query}
             """),
        ]
        ai_msg = default_llm.invoke(messages)
        return f"Search results for: {query}: \n\n\"{ai_msg.content.strip()}\":"
    
search_tool = WebSearch()
# target to compare user input to
target = "MongoDB"
target_context = """
## MongoDB Partner Ecosystem

**Who are they?**

* **Technology Partners:** Provide complementary products and services that integrate with MongoDB.
* **Consulting Partners:** Offer professional services like implementation, migration, and optimization.
* **Cloud Partners:** Provide MongoDB Atlas as a managed service on their cloud platforms.

## MongoDB Mission and Unique Differentiators
MongoDB is built on a scale-out architecture that has become popular with developers of all kinds for developing scalable applications with evolving data schemas. 
As a document database, MongoDB makes it easy for developers to store structured or unstructured data. It uses a JSON-like format to store documents.

### Mission
* To empower developers to build the next generation of intelligent applications.

### Unique Differentiators
* **Document-Oriented Data Model:** Stores data in flexible JSON-like documents, making it easier to represent complex relationships.
* **Schema-Agnostic:** Allows for dynamic data structures, accommodating evolving requirements without rigid schemas.
* **Horizontal Scalability:** Easily scales to handle massive datasets and high traffic loads.
* **High Availability:** Ensures data durability and reliability through replication and sharding.
* **Rich Query Language:** Supports powerful querying and aggregation capabilities, enabling complex data analysis.
* **Strong Community and Ecosystem:** Benefits from a large and active community, providing extensive resources and support.
* **Multi-Cloud Flexibility:** Deploys seamlessly across various cloud platforms, offering choice and portability.
* **Integration with Modern Technologies:** Integrates well with popular programming languages, frameworks, and tools.
"""
# Flask configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your secret key


class CustomCrew:
    def __init__(self, company_name):
        self.company_name = company_name

    def run(self):
       # Define agent with a more specific role and backstory
        custom_agent_1 = Agent(
            role="Partner Compatibility Analyst",
            backstory="I am an expert in assessing the suitability of potential business partners.",
            goal=f"Research the {self.company_name}, its products, and its latest news to determine compatibility as PARTNER.",
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=default_llm,
            memory=True, # Enable memory
            cache=True, # Enable cache
        )

        # Generate a more relevant search query using keyword extraction or semantic search

        custom_task_1 = Task(
            description=dedent(
                "\n\n[additional context]"+target_context+"\n\n[end additional context]"+"\n\n"+
                f"""          
[task]
    Use the research on your web search to create a concise HTML report with structured data and a clear recommendation.
    Search the web researching {self.company_name}, and generate a concise HTML response. 
    Do your best to generate a response with your web research without overusing your tools [IMPORTANT]
    Your recommendation from be from the perspective of {self.company_name}.
[IMPORTANT]
- KEEP YOUR RESPONSE TO 600 CHARACTERS! IMPORTANT!
- ALWAYS TRY TO ANSWER THE QUESTION IN A CLEAR AND CONCISE MANNER.
- BE CONSERVATIVE WITH YOUR TOOL USE. DO NOT OVERUSE IT. 
- CHOOSE FROM THESE QUERIES TO USE FOR YOUR SEARCH TOOL:
    - {self.company_name} + company recent news
    - {self.company_name} + company partnership partner
- IMPORTANT! AFTER A FEW SEARCHES, ATTEMPT TO RESPOND TO THE BEST OF YOUR ABILITY. DO NOT OVERUSE YOUR TOOLS!
    
"""
            ),
            agent=custom_agent_1,
            expected_output="""
concise HTML report with structured data and a clear recommendation. 
The HTML string will be injected into a `<div>`       

IMPORTANT! FOLLOW THE TEMPLATE STRUCTURE BELOW:
[template]
<h2>{self.company_name} - {target} [🔴 | 🟡 | 🟢]</h2>
<p>...</p>
<table>
<tbody>
    <tr>
    <th>Reputation</th>
    </tr>
    <tr>
    <td>Industry Reputation</td>
    <td>[🔴 | 🟡 | 🟢] ...</td>
    </tr>
    <tr>
    <td>Financial Stability</td>
    <td>[🔴 | 🟡 | 🟢] ...</td>
    </tr>
    <tr>
    <td>Compliance</td>
    <td>[🔴 | 🟡 | 🟢] ...</td>
    </tr>
    <tr>
    <th colspan="2">Goals</th>
    </tr>
    <tr>
    <td>Strategic Goals</td>
    <td>[🔴 | 🟡 | 🟢] ...</td>
    </tr>
    <tr>
    <td>Innovation</td>
    <td>[🔴 | 🟡 | 🟢] ...</td>
    </tr>
</tbody>
</table>
[end template]

[response criteria]
- HTML Structure must match the template! IMPORTANT!
- MUST BE RAW HTML STRING! IMPORTANT!
- USE EMOJIS! For High, Medium, and Low, use emojis not words.
- High = 🔴, Medium = 🟡, Low = 🟢. DO NOT USE WORDS!
- YOUR HTML MUST USE BOOTSTRAP CSS.
- MAX RESPONSE LENGTH = 600 CHARACTERS.
- DO NOT INCLUDE <html> or <body> or things like that, just the raw HTML string that can be injected into a <div>
[end response criteria]

[example response for company `ORACLE`]
<h2>ORACLE - {target} [🔴]</h2>
<p>Oracle is a global provider of database technology and enterprise resource planning software. The company has demonstrated financial stability, solid revenue streams, and profitability. However, it's market leadership in the cloud and license segment does not align with our strategic goals and objectives.</p>
<table class="table table-striped">
<tbody>
    <tr>
    <th>Reputation</th>
    </tr>
    <tr>
    <td>Industry Reputation</td>
    <td>🟡</td>
    </tr>
    <tr>
    <td>Financial Stability</td>
    <td>🟢</td>
    </tr>
    <tr>
    <td>Compliance</td>
    <td>🟡</td>
    </tr>
    <tr>
    <th colspan="2">Goals</th>
    </tr>
    <tr>
    <td>Strategic Goals</td>
    <td>🔴</td>
    </tr>
    <tr>
    <td>Innovation</td>
    <td>🟡</td>
    </tr>
</tbody>
</table>
[end example response]
            """,
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
        html_output += "\n"+"<hr />"+"<code>" + str(crew.usage_metrics) + "</code>"
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
            print("\n\n########################")
            print("## Here is your custom crew run result:")
            print("########################\n")
            print(result)
            ai_response = result
            session['reset'] = False

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Research Assistant</title>
        <!-- Bootstrap CSS CDN -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            #video-background {
                position: fixed;
                right: 0;
                bottom: 0;
                min-width: 100%;
                min-height: 100%;
                width: auto;
                height: auto;
                z-index: -100;
            }
            @keyframes fadeIn {
                0% {
                    opacity: 0;
                    transform: translateY(20px);
                }
                100% {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            @keyframes sending {
                0% { opacity: 1; }
                50% { opacity: 0.5; }
                100% { opacity: 1; }
            }
            .sending {
                animation: sending 1s infinite;
                color: #999;
            }
            @keyframes wowEffect {
                0% { transform: scale(1); }
                50% { transform: scale(1.1); }
                100% { transform: scale(1.1); }
            }
            .card-body,.card{
                border-radius:2em;
            }
            .card-body-response {
                animation: wowEffect 0.5s;
            }
            @keyframes pulse {
                0% {
                    transform: scale(1);
                }
                50% {
                    transform: scale(1.05);
                }
                100% {
                    transform: scale(1);
                }
            }
            #send-button {
                animation: pulse 1s infinite;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
            }
            #reset-button {
                animation: pulse 1s infinite;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
            }
            .alert {
                animation: fadeIn 1s;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            }
            .card {
                box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
            }
            .alert-secondary{
                background-color: #f8f9fa;
                border-color: #f8f9fa;
            }
        </style>
        
    </head>
    <body>
        <video autoplay loop muted id="video-background">
            <source src="https://cdn.pixabay.com/video/2019/04/27/23087-333074572_large.mp4" type="video/mp4">
        </video>
        <div class="container py-5">
            <div class="row">
                <div class="col-lg-12 mx-auto">
                    <div class="card">
                        <div id="card-body" class="card-body">
                            <img class="mb-4" style="border:2px solid black;width:90px;border-radius:1em;" src="https://github.com/ranfysvalle02/blog-drafts/blob/main/59731.jpg?raw=true" alt="logo"/>
                            <code>agent-r</code>
                            
                            <div id="chatbox" class="mb-4">
                                {% if ai_response %}
                                <div class="alert alert-secondary" role="alert">
                                    {{ ai_response|safe }}
                                </div>
                                {% endif %}
                            </div>
                            <form method="POST" onsubmit="onFormSubmit()">
                                <div class="form-group">
                                    <input id="user-input" name="user-input" type="text" class="form-control" placeholder="Enter company you want to know about...">
                                </div>
                                <button id="send-button" type="submit" class="btn btn-primary">Start Research</button>
                                <button id="reset-button" name="reset" type="submit" class="btn btn-secondary" style="display: none;">Reset</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Bootstrap JS and jQuery CDN -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
        <script>
        window.onload = function() {
            var reset = {{ 'true' if reset else 'false' }};
            if (reset) {
                document.getElementById("send-button").style.display = "";
                document.getElementById("reset-button").style.display = "none";
                document.getElementById("user-input").style.display = "";
            } else {
                document.getElementById("send-button").style.display = "none";
                document.getElementById("reset-button").style.display = "";
                document.getElementById("user-input").style.display = "none";
            }
            if ({{ 'true' if ai_response else 'false' }}) {
                document.getElementById("card-body").classList.add("card-body-response");
            }
            document.getElementById("card-body").addEventListener('animationend', function() {
                this.style.transform = "scale(1.1)";
            });
        }

        function onFormSubmit() {
            var sendButton = document.getElementById("send-button");
            sendButton.disabled = true;
            sendButton.innerText = "performing research. please wait...";
            sendButton.classList.add("sending");
        }
        </script>
    </body>
    </html>
    ''', user_input=user_input, ai_response=ai_response, reset=session.get('reset', True))

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8080, debug=True)
