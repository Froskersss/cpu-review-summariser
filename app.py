from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import json
import os

app = Flask(__name__)

# Load data from CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), 'data', 'final_data_with_images.csv')
df = pd.read_csv(CSV_PATH, index_col=0)

# Load review links from JSON
LINKS_PATH = os.path.join(os.path.dirname(__file__), 'data', 'review_links.json')
try:
    with open(LINKS_PATH, 'r') as f:
        review_links = json.load(f)
except:
    review_links = {}

# Prepare CPU lists by manufacturer
amd_cpus = df[df['Manufacture'] == 'AMD']['CPU'].tolist()
intel_cpus = df[df['Manufacture'] == 'INTEL']['CPU'].tolist()

def get_cpu_data(cpu_name):
    """Get CPU data from dataframe by name"""
    try:
        row = df[df['CPU'] == cpu_name].iloc[0]
        return {
            'name': row['CPU'],
            'review': row['CPU review'],
            'summary': row['Summarised_review'],
            'image': row['CPU images'],
            'manufacturer': row['Manufacture']
        }
    except:
        return None

@app.route('/')
def index():
    """Home page with CPU list and dropdown"""
    cpu_images = [img for img in df['CPU images'].tolist() if pd.notna(img)]
    
    return render_template('index.html',
                         intel_cpus=intel_cpus,
                         amd_cpus=amd_cpus,
                         cpu_images=cpu_images)

@app.route('/search', methods=['POST'])
def search():
    """Handle search form submission"""
    search_query = request.form.get('search_cpu', '').strip()
    
    # Look for matching CPU
    matching_cpus = df[df['CPU'].str.contains(search_query, case=False, na=False)]['CPU'].tolist()
    
    if matching_cpus:
        # Redirect to the first matching CPU's summary
        return redirect(url_for('cpu_summary', cpu_name=matching_cpus[0]))
    else:
        # Redirect back to home if no match found
        return redirect(url_for('index'))

@app.route('/cpu/<cpu_name>')
def cpu_detail(cpu_name):
    """Display review links page for a specific CPU"""
    cpu_data = get_cpu_data(cpu_name)
    
    if not cpu_data:
        return redirect(url_for('index'))
    
    # Get review URLs from links file
    cpu_links = review_links.get(cpu_name, {})
    techpowerup_url = cpu_links.get('techpowerup', None)
    techspot_url = cpu_links.get('techspot', None)
    
    return render_template('cpu.html',
                         cpu_name=cpu_data['name'],
                         manufacturer=cpu_data['manufacturer'],
                         cpu_img=f"static/{cpu_data['image']}",
                         techpowerup_url=techpowerup_url,
                         techspot_url=techspot_url)

@app.route('/cpu/<cpu_name>/summary')
def cpu_summary(cpu_name):
    """Display summary for a specific CPU"""
    cpu_data = get_cpu_data(cpu_name)
    
    if not cpu_data:
        return redirect(url_for('index'))
    
    return render_template('cpu_summary.html',
                         cpu_name=cpu_data['name'],
                         summary=cpu_data['summary'],
                         cpu_img=f"static/{cpu_data['image']}",
                         manufacturer=cpu_data['manufacturer'])

@app.route('/cpu-list')
def cpu_list():
    """Display all CPUs in a list format"""
    cpus_data = []
    for cpu_name in df['CPU'].tolist():
        cpus_data.append(get_cpu_data(cpu_name))
    
    return render_template('cpu_list.html', cpus=cpus_data)

if __name__ == '__main__':
    app.run(debug=True)
