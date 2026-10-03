"""All site copy + business details live here. Edit this file, re-run build.py."""

BIZ = {
    'name': 'Rapid Rescue & Recovery',
    'short': 'Rapid Rescue',
    'domain': 'https://rapidrescuerecovery.co.uk',
    'phone_display': '07376 322865',
    'phone_tel': '+447376322865',
    'wa': '447376322865',
    'email': 'info@rapidrescuerecovery.co.uk',
    'base': 'Telford',
    'region': 'Shropshire',
    'is_24_7': True,                 # <-- CONFIRM with client before launch
    'hours_text': 'Open 24 hours, 7 days a week',
    'payment': 'Card, Apple Pay, Google Pay, bank transfer & cash',   # <-- CONFIRM
    'vehicles': 'Cars, vans up to 3.5t, 4x4s, SUVs, electric & hybrid vehicles',  # <-- CONFIRM vs truck spec
    'google_review_url': '',          # paste the Google "Ask for reviews" link once GBP is verified
    'socials': {                      # fill in once handles are claimed; empty = hidden
        'facebook': '',
        'instagram': '',
        'tiktok': '',
    },
}

WA_DEFAULT = "Hi Rapid Rescue, I need help with my vehicle.\n\nLocation: \nVehicle: \nWhat's wrong: \nWhere it needs to go: "

# ---------------------------------------------------------------------------
# SERVICES
# ---------------------------------------------------------------------------
SERVICES = [
 {
  'slug': 'breakdown-recovery', 'icon': 'truck', 'name': 'Breakdown Recovery',
  'card': 'Engine died, clutch gone or warning lights on? We load it up and take it home, to your garage or anywhere you choose.',
  'title': 'Breakdown Recovery Telford | 24/7 Car & Van Recovery | Rapid Rescue',
  'desc': '24/7 breakdown recovery in Telford, Shropshire and UK-wide. Pay as you go, no membership needed. Fixed quote before we move. Call 07376 322865.',
  'h1': 'Breakdown recovery in Telford, Shropshire & UK-wide',
  'lead': "Broken down at home, at work or at the side of the road? You don't need a membership. Call or WhatsApp, get a fixed price, and we'll come and get you.",
  'body': [
    ('h2', 'Pay-as-you-go breakdown recovery, no membership needed'),
    ('p', "Most people who call us don't have breakdown cover, or their cover has run out, or the wait they've been quoted is too long. That's fine. We're a one-off recovery service: you pay for the job you need, nothing more, and you get a price before we set off."),
    ('p', "We recover cars, vans up to 3.5 tonnes, 4x4s, SUVs, automatics, and electric and hybrid vehicles. Everything is carried <strong>fully on the bed of our recovery truck</strong>, not towed on its wheels. That's the safe way to move an automatic or an EV, and it means no extra wear on a car that's already got a problem."),
    ('h2', 'Common breakdowns we recover'),
    ('ul', ["Engine won't start or cuts out while driving", "Clutch, gearbox or driveshaft failure", "Overheating, coolant leaks or a snapped cambelt", "Dashboard warning lights where it's not safe to keep driving", "Electrical faults and flat batteries that won't jump", "Wrong fuel: <em>don't start the engine</em>, call us", "Flat tyre with no spare or locking wheel nut key"]),
    ('h2', 'Where can we take your vehicle?'),
    ('p', "Wherever you need it to go: your home, your local garage, a main dealer, a specialist, or a garage across the country. If you're not sure where to take it, tell us what's wrong and we can suggest options nearby."),
  ],
  'faqs': [
    ("Do I need breakdown cover to use you?", "No. We're pay-as-you-go. Call or WhatsApp us, we'll give you a fixed price for the job, and you only pay for that recovery."),
    ("Can you recover automatic and electric cars?", "Yes. Your vehicle is carried fully on the bed of our truck, which is the recommended way to move automatics, 4x4s and EVs, because none of the wheels turn."),
    ("Can I travel with my car?", "In most cases there's room in the cab for passengers. Just tell us how many people there are when you call so we can plan for it."),
  ],
 },
 {
  'slug': 'accident-recovery', 'icon': 'crash', 'name': 'Accident Recovery',
  'card': "After a collision, we clear your vehicle from the scene and take it home, to a bodyshop or to wherever your insurer asks.",
  'title': 'Accident Recovery Telford & Shropshire | 24/7 | Rapid Rescue',
  'desc': 'Accident and collision recovery in Telford, Shropshire and across the UK. Careful loading, photos of your vehicle, delivered to home, bodyshop or storage. Call 07376 322865.',
  'h1': 'Accident recovery: calm, careful and quick',
  'lead': "After a collision, the last thing you need is a long wait. We'll get your vehicle off the road safely and take it wherever it needs to go.",
  'body': [
    ('h2', 'First things first'),
    ('p', "If anyone is hurt, or vehicles are blocking a live lane, <strong>call 999 first</strong>. Once everyone's safe and the emergency services are happy, call or WhatsApp us with your location and we'll take it from there."),
    ('h2', 'What we do at the scene'),
    ('ul', ["Load damaged and non-rolling vehicles safely using winch, skates and dollies", "Clear loose debris from the vehicle before we move it", "Take photos of your vehicle before and after loading and send them to your WhatsApp, which is useful for your insurer", "Deliver to your home, a bodyshop, a garage or wherever your insurer tells you"]),
    ('h2', 'Dealing with your insurer'),
    ('p', "Some insurers arrange their own recovery and some will reimburse you for using your own. If you're not sure, check your policy or call your insurer. We'll give you a clear itemised invoice and the photos, so a claim is easy."),
  ],
  'faqs': [
    ("Can you recover a car that won't roll or steer?", "Yes. Tell us when you call. We bring the right equipment to load vehicles with locked wheels, collapsed suspension or steering damage."),
    ("Will my insurance pay for the recovery?", "It depends on your policy. Many fully comprehensive policies cover recovery after an accident. We'll give you an itemised invoice and photos for your claim."),
  ],
 },
 {
  'slug': 'motorway-recovery', 'icon': 'road', 'name': 'Motorway & Roadside Recovery',
  'card': "Stuck on the M54, M6, A5 or A442? Get yourself safe, then send us your pin. We know these roads.",
  'title': 'M54 & Motorway Recovery Telford | M6, A5, A442 | Rapid Rescue',
  'desc': 'Motorway and roadside recovery on the M54, M6, A5, A442 and A41 around Telford, Shropshire and Wolverhampton. Send your location on WhatsApp. Call 07376 322865.',
  'h1': 'Motorway & roadside recovery on the M54, M6, A5 & A442',
  'lead': "Breaking down on a fast road is frightening. Get yourself safe first, then send us your exact location and we'll get to you as quickly as we safely can.",
  'body': [
    ('callout', "<strong>Stopped in a live lane, or can't get out safely?</strong> Stay in your vehicle with your seatbelt on and hazard lights on, and call <a href=\"tel:999\">999</a> straight away. On motorways you can also call National Highways on <a href=\"tel:03001235000\">0300 123 5000</a>."),
    ('h2', 'Roads we cover every day'),
    ('p', "Our base is in Telford, right next to the <strong>M54</strong>, so we're close to junctions 1 to 7, the <strong>M6</strong> around Wolverhampton and Cannock, the <strong>A5</strong> to Shrewsbury, the <strong>A442</strong> Queensway, the <strong>A41</strong> to Newport and Whitchurch, and the <strong>A464</strong> and <strong>A518</strong>."),
    ('h2', 'Help us find you fast'),
    ('ul', ["Tap <strong>Send my location</strong> on this page and your GPS pin goes straight to our WhatsApp", "On a motorway, look for the <strong>marker posts</strong> (small blue and white signs every 100m) and tell us the number and direction", "Tell us the junctions you're between and which carriageway (e.g. M54 eastbound between J4 and J3)", "Wait behind the barrier, well away from your vehicle and the traffic"]),
    ('p', 'Read our full guide: <a href="/broken-down/">What to do if you break down</a>.'),
  ],
  'faqs': [
    ("Can you come to the motorway?", "Yes, for vehicles in a safe place such as the hard shoulder, an emergency area or a slip road. If you're in a live lane, call 999 first. Sometimes the police or National Highways arrange the removal themselves."),
    ("How do I tell you where I am on a motorway?", "Use the Send my location button, or tell us the number on the nearest marker post, the road, the direction and the junctions you're between."),
  ],
 },
 {
  'slug': 'jump-start', 'icon': 'battery', 'name': 'Jump Starts & Flat Batteries',
  'card': "Flat battery at home, work or in a car park? We'll come and jump-start you, and recover it if it still won't go.",
  'title': 'Jump Start Telford | Flat Battery Help 24/7 | Rapid Rescue',
  'desc': 'Flat battery? Mobile jump-start service in Telford, Shrewsbury and Shropshire, at home, at work or in a car park. If it still won\'t start, we\'ll recover it. Call 07376 322865.',
  'h1': 'Jump starts & flat battery call-outs',
  'lead': "Car dead on the drive or in a car park? We'll come out with a professional booster pack and get you going. If it still won't start, we can recover it there and then.",
  'body': [
    ('h2', 'Signs it\'s your battery'),
    ('ul', ["Clicking, or nothing at all, when you turn the key or press start", "Dim dashboard lights or interior lights", "The car was left with lights on or hasn't been driven for a while", "Cold mornings, when weak batteries usually give up first"]),
    ('h2', "If it won't start"),
    ('p', "Not every no-start is a battery. If a jump doesn't fix it, you don't have to call anyone else: we can load it up there and then and take it to a garage of your choice."),
    ('h2', 'Where we come out to'),
    ('p', "Home driveways, workplaces, supermarket and multi-storey car parks, train stations and retail parks across Telford, Shrewsbury, Newport, Shifnal, Bridgnorth and the surrounding area. Let us know about any height limits so we can plan."),
  ],
  'faqs': [
    ("Is a jump start bad for modern cars?", "Not when it's done properly. We use a professional booster pack and follow the right connection points for your vehicle, including stop-start and hybrid systems."),
    ("Do you sell batteries?", "If your battery needs replacing, we can take the car to a local garage or battery specialist. Ask when you call."),
  ],
 },
 {
  'slug': 'vehicle-transport', 'icon': 'route', 'name': 'Vehicle Transport & Delivery',
  'card': "Bought a car miles away? Moving house? Auction or dealer collection? We'll move it for you, locally or anywhere in the UK.",
  'title': 'Car Transport & Vehicle Delivery UK | Auction Collections | Rapid Rescue',
  'desc': 'Car transport and vehicle delivery from Telford and Shropshire to anywhere in the UK. Private purchases, auction and dealer collections, house moves. Get a fixed quote. 07376 322865.',
  'h1': 'Vehicle transport & delivery, locally or UK-wide',
  'lead': "Not every job is an emergency. When you need a vehicle moved from A to B without putting miles on it, we'll collect it, carry it and deliver it, with photos at both ends.",
  'body': [
    ('h2', 'What we move'),
    ('ul', ["Cars bought privately or from dealers anywhere in the UK", "Auction collections", "Dealer-to-dealer and dealer-to-customer deliveries", "Classic, prestige, lowered and track cars that shouldn't be driven", "Project cars, SORN vehicles and cars without MOT", "House moves, and taking a car to a new owner"]),
    ('h2', 'How it works'),
    ('p', "Tell us the collection and delivery addresses, the vehicle, and when it needs to move. We'll give you a fixed price. On the day, we photograph the vehicle at collection, keep you updated on WhatsApp and send photos on delivery."),
    ('h2', 'Regular moves? Open a trade account'),
    ('p', 'If you\'re a dealer, garage or bodyshop moving vehicles every week, see our <a href="/trade-accounts/">trade accounts</a>.'),
  ],
  'faqs': [
    ("How far will you go?", "Anywhere in mainland UK. Longer journeys are priced by distance. Ask for a quote with both postcodes."),
    ("Can I book in advance?", "Yes. Scheduled transport can be booked days or weeks ahead. Message us the details and your preferred date."),
  ],
 },
 {
  'slug': 'non-runner-collection', 'icon': 'key', 'name': 'Non-Runners & Garage Runs',
  'card': "Car that hasn't moved in months? Needs to get to the MOT, the garage or a new home? We'll collect it.",
  'title': 'Non-Runner Car Collection & Garage Runs Telford | Rapid Rescue',
  'desc': 'Non-runner vehicle collection, MOT and garage runs in Telford and Shropshire. SORN, project and stored cars moved safely. Fixed quote. Call or WhatsApp 07376 322865.',
  'h1': 'Non-runner collection, MOT & garage runs',
  'lead': "Whether it's sat on the drive for a year or it just isn't safe to drive to the garage, we'll pick it up and drop it where it needs to be.",
  'body': [
    ('h2', 'Typical jobs'),
    ('ul', ["Taking a non-runner to the garage for repair", "MOT runs for cars with known faults or no current MOT", "Collecting cars from storage, barns, garages and driveways", "Moving project cars between workshops", "Returning repaired cars to the owner"]),
    ('h2', 'Tricky access? Tell us'),
    ('p', "Flat tyres, seized brakes, no keys, tight driveways or underground car parks. Let us know when you get in touch (photos on WhatsApp help a lot) and we'll bring the right kit."),
  ],
  'faqs': [
    ("Can you move a car with flat tyres or seized brakes?", "Usually, yes. We use skates and a winch for vehicles that won't roll. Send us a photo on WhatsApp so we can bring the right kit."),
    ("Do I need to be there?", "Not always. If the keys and access are arranged, we can collect and send you photos when it's loaded and when it's delivered."),
  ],
 },
]

# ---------------------------------------------------------------------------
# AREAS
# ---------------------------------------------------------------------------
AREAS = [
 {
  'slug': 'telford', 'name': 'Telford', 'local': True,
  'title': 'Car Recovery Telford | 24/7 Breakdown Recovery | Rapid Rescue',
  'desc': 'Local 24/7 car and van recovery in Telford: Wellington, Madeley, Oakengates, Donnington, Priorslee and more. Fixed quote before we move. Call 07376 322865.',
  'h1': 'Car & van recovery in Telford',
  'lead': "Telford is home. Wherever you've broken down in the borough, from Wellington to Madeley and Donnington to Ironbridge, we're close by.",
  'body': [
    ('p', "We're based in Telford, so we know the town's roads: the M54 from junction 4 to 7, the A442 Queensway, the A5 and A518, and all the roundabouts in between. We regularly recover from the town centre, retail parks and industrial estates including <strong>Hortonwood, Stafford Park and Halesfield</strong>."),
    ('h2', 'Telford areas we cover'),
    ('chips', ['Wellington', 'Oakengates', 'Madeley', 'Dawley', 'Donnington', 'Hadley', 'Ketley', 'Lawley', 'Priorslee', 'Ironbridge', 'Stirchley', 'Brookside', 'Sutton Hill', 'Woodside', 'Hollinswood', 'Trench', 'Leegomery', 'Admaston', 'Horsehay', 'Muxton', "St George's", 'Telford Town Centre']),
    ('h2', 'What we do in Telford'),
    ('p', 'Breakdown and accident recovery, jump starts, non-runner collections, MOT and garage runs, and vehicle transport anywhere in the UK. <a href="/contact/">Get a quote</a> or tap Send my location.'),
  ],
 },
 {
  'slug': 'shrewsbury', 'name': 'Shrewsbury', 'local': True,
  'title': 'Car Recovery Shrewsbury | Breakdown & Vehicle Recovery | Rapid Rescue',
  'desc': 'Breakdown and car recovery in Shrewsbury and on the A5 and A49: Battlefield, Harlescott, Meole Brace, Monkmoor and more. Call or WhatsApp 07376 322865.',
  'h1': 'Car recovery in Shrewsbury',
  'lead': "Broken down in Shrewsbury or on the A5 between Telford and the county town? We're straight down the road.",
  'body': [
    ('p', "Shrewsbury is a short run along the A5 from our Telford base. We cover the town and the main routes in and out, including the <strong>A5 and A49 bypass</strong>, the A458 towards Welshpool, the A528 and the A53 towards Shawbury and Market Drayton."),
    ('h2', 'Shrewsbury areas we cover'),
    ('chips', ['Battlefield', 'Harlescott', 'Sundorne', 'Monkmoor', 'Castlefields', 'Frankwell', 'Copthorne', 'Meole Brace', 'Bayston Hill', 'Belle Vue', 'Kingsland', 'Bicton Heath', 'Atcham', 'Shrewsbury Town Centre']),
    ('h2', 'Taking it back to Telford, or anywhere else'),
    ('p', 'We can take your vehicle to a garage in Shrewsbury, back home, or to a dealer anywhere in the UK. <a href="/contact/">Request a quote</a>.'),
  ],
 },
 {
  'slug': 'wolverhampton', 'name': 'Wolverhampton', 'local': True,
  'title': 'Car Recovery Wolverhampton | M54 & M6 Breakdown Recovery | Rapid Rescue',
  'desc': 'Breakdown recovery in Wolverhampton and on the M54, M6 and A41/A449: Tettenhall, Codsall, Pendeford, Wednesfield and i54. Call or WhatsApp 07376 322865.',
  'h1': 'Car recovery in Wolverhampton',
  'lead': "From the M54 junction 1 and 2 to the ring road, we cover Wolverhampton and the west side of the Black Country.",
  'body': [
    ('p', "Wolverhampton is at the eastern end of the M54, so it's a straight run from our base. We cover the city, the <strong>M54 junctions 1 to 3</strong>, the <strong>M6</strong> around junctions 10 to 12, the A449, A41, A454 and A460, and the business parks around <strong>i54</strong>."),
    ('h2', 'Wolverhampton areas we cover'),
    ('chips', ['Tettenhall', 'Codsall', 'Pendeford', 'Fordhouses', 'Wednesfield', 'Bilston', 'Penn', 'Whitmore Reans', 'Bushbury', 'Albrighton', 'Perton', 'i54', 'City Centre']),
    ('h2', 'Bought a car in the Black Country?'),
    ('p', 'We regularly move vehicles between the West Midlands and Shropshire. See <a href="/services/vehicle-transport/">vehicle transport</a>.'),
  ],
 },
 {
  'slug': 'newport', 'name': 'Newport', 'local': True,
  'title': 'Car Recovery Newport Shropshire | Breakdown Recovery | Rapid Rescue',
  'desc': 'Breakdown and vehicle recovery in Newport, Shropshire and on the A41 and A518: Edgmond, Church Aston, Chetwynd and Harper Adams. Call 07376 322865.',
  'h1': 'Car recovery in Newport, Shropshire',
  'lead': "Newport is just up the A518 from Telford, so help isn't far away.",
  'body': [
    ('p', "We cover Newport town, the surrounding villages and the <strong>A41</strong> north towards Whitchurch and south towards the M54. That includes Harper Adams University. If you're a student whose car has given up, we'll get it sorted."),
    ('h2', 'Newport areas we cover'),
    ('chips', ['Newport Town', 'Edgmond', 'Church Aston', 'Chetwynd', 'Lilleshall', 'Tibberton', 'Harper Adams', 'Forton', 'Gnosall']),
  ],
 },
 {
  'slug': 'bridgnorth', 'name': 'Bridgnorth', 'local': True,
  'title': 'Car Recovery Bridgnorth | Breakdown Recovery | Rapid Rescue',
  'desc': 'Breakdown and car recovery in Bridgnorth and on the A442, A458 and A454: High Town, Low Town and surrounding villages. Call or WhatsApp 07376 322865.',
  'h1': 'Car recovery in Bridgnorth',
  'lead': "Down the A442 from Telford, Bridgnorth and the Severn Valley villages are well within our local area.",
  'body': [
    ('p', "We cover Bridgnorth's High Town and Low Town and the routes in and out: the <strong>A442</strong> to Telford and Kidderminster, the <strong>A458</strong> towards Shrewsbury and Stourbridge, and the <strong>A454</strong> to Wolverhampton. The country lanes can be tight, so tell us about access and we'll plan for it."),
    ('h2', 'Bridgnorth areas we cover'),
    ('chips', ['High Town', 'Low Town', 'Oldbury', 'Quatford', 'Alveley', 'Highley', 'Worfield', 'Broseley', 'Much Wenlock']),
  ],
 },
 {
  'slug': 'shifnal', 'name': 'Shifnal', 'local': True,
  'title': 'Car Recovery Shifnal | M54 J3–J4 Breakdown Recovery | Rapid Rescue',
  'desc': 'Breakdown and car recovery in Shifnal and on the M54 J3 and J4, A464 and A41: Albrighton, Cosford and surrounding villages. Call 07376 322865.',
  'h1': 'Car recovery in Shifnal',
  'lead': "Sitting between junctions 3 and 4 of the M54, Shifnal is only minutes from our base.",
  'body': [
    ('p', "We cover Shifnal town, the <strong>A464</strong> into Telford, the <strong>A41</strong> around Albrighton and Cosford, and the M54 in both directions."),
    ('h2', 'Shifnal areas we cover'),
    ('chips', ['Shifnal Town', 'Albrighton', 'Cosford', 'Tong', 'Weston-under-Lizard', 'Beckbury', 'Sheriffhales']),
  ],
 },
 {
  'slug': 'nationwide', 'name': 'UK-wide', 'local': False,
  'title': 'Nationwide Vehicle Recovery & Transport | UK-wide | Rapid Rescue',
  'desc': 'UK-wide breakdown recovery and vehicle transport. One number, one point of contact: our own trucks locally, and trusted partner operators across the country. 07376 322865.',
  'h1': 'Nationwide recovery & vehicle transport',
  'lead': "Broken down far from home? Need a car moved from the other end of the country? You only need one number: ours.",
  'body': [
    ('h2', 'How our UK-wide service works'),
    ('p', "Around Telford, Shropshire and the West Midlands, we come out ourselves. Further afield, we arrange your recovery through <strong>trusted partner operators</strong> across the country, so you get local help fast, without having to ring round strangers at the roadside."),
    ('ul', ["<strong>One point of contact:</strong> you deal with us from first call to drop-off", "<strong>Fixed price agreed upfront</strong> before anyone sets off", "<strong>WhatsApp updates</strong> so you know who's coming and when", "<strong>Brought home to Shropshire</strong>: if you've broken down away from home, we can arrange for you and your vehicle to be brought back"]),
    ('h2', 'Long-distance vehicle transport'),
    ('p', 'Bought a car in Scotland, Cornwall or anywhere in between? We\'ll collect and deliver it. See <a href="/services/vehicle-transport/">vehicle transport</a>.'),
  ],
 },
]

# ---------------------------------------------------------------------------
# HOME FAQ
# ---------------------------------------------------------------------------
HOME_FAQS = [
 ("How quickly can you get to me?", "It depends on where you are, the time of day and the traffic. We'll give you an honest arrival time when you call, and keep you updated on WhatsApp so you're never left guessing."),
 ("How much does vehicle recovery cost?", "Every job is different, so we give you a <strong>fixed price before we set off</strong>. The price depends on distance, time of day, the vehicle and how easy it is to load. No hidden extras, no surprises."),
 ("Do I need to be a member or have breakdown cover?", "No. We're pay-as-you-go. Call or WhatsApp, agree the price, and that's it."),
 ("Do you cover outside Telford?", "Yes. We cover Telford, Shropshire and the West Midlands with our own truck, and anywhere in the UK through our trusted partner network, with one point of contact throughout."),
 ("What vehicles can you recover?", "Cars, vans up to 3.5 tonnes, 4x4s, SUVs, automatics, and electric and hybrid vehicles. Everything is carried fully on the bed of our truck, which is the safest way to move them."),
 ("Where can you take my vehicle?", "Anywhere you need: your home, a local garage, a main dealer, a bodyshop, or a destination anywhere in the UK."),
 ("How do I pay?", "Card, Apple Pay, Google Pay, bank transfer or cash. You'll get a clear invoice for every job."),
 ("Do you work with garages and car dealers?", 'Yes. We run regular collections and deliveries for garages, dealers and bodyshops. See <a href="/trade-accounts/">trade accounts</a>.'),
]
