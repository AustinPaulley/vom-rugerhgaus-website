import os
from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a secure environment variable
@app.route('/')
def index():
    dogs = [
        {'name': 'Harmony', 'filename': 'Harmony.jpg'},
        {'name': 'Lady',    'filename': 'Lady.jpg'},
        {'name': 'Fang',    'filename': 'Fang.jpg'},
        {'name': 'Magnum',  'filename': 'Magnum.jpg'}
    ]
    return render_template('index.html', dogs=dogs)
@app.route('/training')
def training():
    gallery_dir = os.path.join(app.static_folder, 'images', 'gallery')
    photos = [f for f in os.listdir(gallery_dir)
              if f.lower().endswith(('.png','.jpg','.jpeg','.gif'))]
    return render_template('training.html', photos=photos)
@app.route('/studs')
def studs():
    photos = ['Magnum1.jpg', 'Magnum2.jpg']
    return render_template('studs.html', photos=photos)
@app.route('/females')
def females():
    female_data = [
        {
            'name': 'Fang',
            'photos': ['Fang1.jpg', 'Fang2.jpg'],
            'pedigree': [
                'SG Fang Canine Extreme WB',
                'Sire: VA2 (A-SVÖ 2022) Zamp Von Aurelius IGP3 KKL',
                'Dam: V Daphne Vom Holtkamper Hof IGP1 KKL' ,
                'OFA Good Hips' ,
                'OFA Normal Elbows'
            ]
        },
        {
            'name': 'Lady',
            'photos': ['Lady1.jpg'],
            'pedigree': [
                'Currently training in Germany',
                'SG1 Leading Lady Canine Extreme WB',
                'Sire: V(BSZS) Indoctro Canine Extreme IGP3 KKL',
                'Dam: V Friedchen v.d. Burg Reichenstein IGP1 KKL',
                'SV HD/ Normal',
                'SV ED/ Normal'
            ]
        },
        {
            'name': 'Harmony',
            'photos': ['Harmony1.jpg', 'Harmony2.jpg'],
            'pedigree': [
                "Chambray’s Rhythm N’ Harmony",
                'Sire: CHAMBRAYS DANTE ALEXANDRE NOY PEREZ',
                'Dam: CHAMBRAYS RHYTHMIC N COUNTER',
                'OFA Good Hips',
                'OFA Normal Elbows',
                'OFA Cardiac/ Normal'
            ]
        },
        {
            'name': 'Blitz',
            'photos': ['Blitz1.jpg'],
            'pedigree': [
                'Retired female',
                'SG1 Geneva Vom Bestinhaus BH',
                "Sire: VA (V43 BSZS 14’) Zigo Vom Regina Pacis IPO2 KKL",
                'Dam: V Quentali vom Finkenschlag IPO1 KKL'
            ]
        }
    ]
    return render_template('females.html', females=female_data)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"New message from {name} ({email}): {message}")
        flash("Message sent successfully!", "success")
        return redirect('/contact')
    return render_template('contact.html')

@app.route('/litters')
def litters():
    litter_data = [
        {
            'photos': ['Seppel.jpg', 'Lola.jpg'],
            'details': [
                "V2 (USA) Seppel vom Holtkamper Hof IGP1 KKL",
                "Pedigree: VA1 Keule vom Holtkamper Hof IPO3 KKL",
                "Pedigree: VA2 Fight vom Holtkamper Hof IPO3 KKL",
                "x",
                "SG Nicholas’ Lola",
                "Pedigree: V Kongo von der Freiheit Westerholt IPO3 KKL",
                "Pedigree: 2× VA Chacco v.d. Freiheit Westerholt SCHH3",
                "Planned pairing with excellent temperament and pedigree"
            ]
        }
    ]
    return render_template('litters.html', litters=litter_data)


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)