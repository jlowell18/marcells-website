# Page content for marcellspaper.com, copied from the GoDaddy site on
# 2026-09-22 (Jared). Edit text here, run tools/build_site.py, push.
# Images: filenames under site/assets/ (see tools/import-images workflow).

IMAGES = {
    "hero": "assets/hero.jpg",
    "logo": "assets/logo.webp",
    "svc_paper": "assets/service-paper.jpg",
    "svc_secure": "assets/service-secure.webp",
    "svc_newpaper": "assets/service-newpaper.webp",
    "services_hero": "assets/services-hero.jpg",
}

PHONE_LINK = '<a href="tel:+17732651200">(773) 265-1200</a>'

HOME = f"""
<div class="hero"><div class="wrap">
  <div>
    <h1>Marcells Paper &amp; Metal</h1>
    <p class="lead">Paper and metal recycling for Chicago-area printers, manufacturers and offices — pickup, containers, secure destruction and top-dollar pricing, all from one family-owned company since the 1970s.</p>
    <div class="cta"><a class="btn" href="contact.html">Request a quote</a><a class="btn ghost" href="services.html">Our services</a></div>
    <p style="margin-top:18px;color:var(--muted)"><strong>Address:</strong> 4221 W Ferdinand, Chicago, IL 60624 &nbsp;&middot;&nbsp; <strong>Phone:</strong> {PHONE_LINK} &nbsp;&middot;&nbsp; <strong>Fax:</strong> (773) 265-1220</p>
  </div>
  <img src="{IMAGES['hero']}" alt="Recycled paper and green recycling arrows">
</div></div>

<section><div class="wrap">
  <h2>Paper and Metal Recycling Solutions You May Need</h2>
  <p class="sub">Three things we do every day for hundreds of Chicago-area businesses.</p>
  <div class="cards">
    <div class="card"><img src="{IMAGES['svc_paper']}" alt="Paper and metal waste moving on a belt">
      <div class="body"><h3>Paper Recycling &amp; Waste Removal</h3>
      <p>MPM excels at assisting clients with smooth and efficient fulfillment and paper waste removal and recycling. We work with a broad spectrum of paper grades from newspaper and corrugated to high grade and pulp. Our direct relationships with the paper mills allow us to work on our clients' best behalf and generate top value for your paper waste.</p>
      <p><strong>Please call us for a free consultation and quote. No job is too big!</strong></p>
      <a class="more" href="paper-recycling.html">Paper recycling &rarr;</a></div></div>
    <div class="card"><img src="{IMAGES['svc_secure']}" alt="Privacy and secure document destruction">
      <div class="body"><h3>Secure Document Destruction</h3>
      <p>MPM understands that the secure destruction of sensitive documents and files is a serious business. That is why we added a special site at our facility dedicated to that process. We offer pick-up services to collect your documents and provide the secure destruction of those files. Our document destruction site is isolated specifically and solely for this purpose.</p>
      <p><strong>24 hour video surveillance with remote viewing access.</strong></p>
      <a class="more" href="services.html">All services &rarr;</a></div></div>
    <div class="card"><img src="{IMAGES['svc_newpaper']}" alt="New paper stock in sheets and rolls">
      <div class="body"><h3>New Paper &amp; Metal Recycling</h3>
      <p>MPM maintains a vast inventory of NEW &amp; JOB LOT paper in cut sheets and rolls from 30pt to 24pt CS2. Stock is available to printers at significant savings. In-stock items vary, so give us a call to inquire about what we currently have.</p>
      <p>We also specialize in metal recycling — aluminum plates, mixed metals and more — with the equipment to strip, load and haul bulky items.</p>
      <a class="more" href="metal-recycling.html">Metal recycling &rarr;</a></div></div>
  </div>
</div></section>

<div class="stat"><h2>EACH TON (2,000 POUNDS) OF RECYCLED PAPER CAN SAVE</h2><p>THREE CUBIC YARDS OF LANDFILL SPACE</p></div>

<section class="alt"><div class="wrap" style="text-align:center">
  <h2>Ready to schedule a pickup?</h2>
  <p class="sub">Same-day service on requests before 10:00 am, and never later than the next day.</p>
  <a class="btn" href="tel:+17732651200">Call (773) 265-1200</a> &nbsp; <a class="btn ghost" href="contact.html">Send a message</a>
</div></section>
"""

ABOUT = [
    ("p", "Back in the mid to late 70’s, Scott Lowell was your average college student. One of the classes he was taking at the time was Statistics 101. On his way to this particular class, he would pass a room designated for computers only. In those days, the computer industry was just entering its humble beginnings and in order to communicate to computers, one would feed them punch-tab cards to deliver information. This process has since been modernized to what we now refer to as hard-drives on present day computers."),
    ("p", "Scott noticed that the used key punch cards were being saved and placed back into the original boxes they came in. He got to talking with someone in the room who explained that a service comes in, buys the punch cards back and takes them away. He further learned that paper mills use the old key punch cards by recycling them into other paper products. He also found out that there were companies in the Chicago area that were also interested in buying them back. Scott discovered the name of such a company, called them up and asked them how much they were paying for scrap computer cards. He was told that they would pay roughly .10 cents per pound or $200 per ton for the tab cards, but that he would have to find a way to bring the cards to their plant. Scott still jokes about the first pick up he ever made, saying that he loaded 10 cases of computer tab cards in the trunk of his old car."),
    ("p", "Scott soon realized that this could be a very good business prospect. He noticed that every Sunday when he opened up the job section of the paper, he would see between 300 and 400 want ads seeking computer analysts. Either the ads would say “Data Processing Managers” or “Computer Analysts” Wanted. Who better to have used computer cards than the companies searching for employees for their computers? Scott wanted to capitalize on the opportunity, but first he needed to do four things: develop a name for his company, open a checking account, get a truck to pick up the scrap computer cards, and hire an answering service to field his phone calls. He figured with all the want ads in the Sunday Papers, the opportunities were endless."),
    ("p", "Perhaps Scott’s biggest business feat to this day was obtaining the financing needed to purchase his first step van for pick-ups. Scott persuaded his grandmother to loan him $1,000 – which he paid back at $50 a month. At that time, Scott’s mother had a small dress shop located on Devon Avenue in Chicago. It was called “Marcells Custom Tailoring”. Scott explains that his mother always answered the phone the same way, “Marcells”. Marcells was the only word she ever said. Not “Marcells Custom Tailoring”, just “Marcells”. His mom said that she could take all of his phone calls and it would sound professional enough that nobody would ever know that he didn’t have the means to afford an office. So therein the name “Marcells Paper and Metal INC” was adopted. Scott also jokes that he used his caddie money from the golf course to open up his first checking account. Bingo! All four things were now completed. Now Scott was a viable one-truck operation and was calling on all sorts of institutions from his stack of newspaper want ads, in search of used computer cards. He offered them .7 cents per pound or $140 per ton to buy them back."),
    ("p", "On off school days, holidays and such, Scott’s 12-year younger brother Jeff got involved, helping him out on the truck. Scott’s mother continued to answer his phone calls at her dress shop. Scott had business cards made up with the address and phone number of the dress shop. So when his mother answered the phones by saying “Marcells”, whether the caller was a customer of the dress shop or Scott’s paper recycling center in Chicago, IL, they had come to the right place!"),
    ("p", f"Now that you know our history, it might be time to get to know Marcells Paper and Metal INC as a paper recycling center. If you’re interested in Marcells Paper and Metal INC and the <a href=\"paper-recycling.html\">paper recycling</a> work we do in Chicago, IL, give us a call at {PHONE_LINK} right away to get the paper recycling services you’re looking for."),
]

EQUIPMENT = f"""
<section><div class="wrap"><div class="prose">
  <h1>Welcome to Marcells Paper &amp; Metal Recycling Center</h1>
  <p><strong>MPM provides a complete onsite analysis to determine the equipment most appropriate for your company’s needs. We service businesses of all sizes and base our proposal on the total tonnage of waste that your facility produces.</strong></p>
  <p><strong>Our equipment specialists create comprehensive programs best suited for the on-site recycling of your waste. These programs will decrease labor costs and will make recycling safer, easier and more profitable. MPM works with you from start to finish in devising a specially tailored equipment plan. We offer equipment financing, installation, waste removal and ongoing customer support.</strong></p>
</div></div></section>
<section class="alt"><div class="wrap">
  <h2>Equipment</h2>
  <p class="sub">Sized to your tonnage, installed by us, supported for the life of the program.</p>
  <div class="gallery">
    <figure><img src="assets/eq-balers.jpg" alt="Balers"><figcaption>Balers</figcaption></figure>
    <figure><img src="assets/eq-conveyors.jpg" alt="Conveyors"><figcaption>Conveyors</figcaption></figure>
  </div>
  <h2 style="margin-top:36px">Containers</h2>
  <p class="sub">From Gaylord boxes and collapsible containers to black bin receptacles and spotted trailers.</p>
  <div class="gallery">
    <figure><img src="assets/eq-containers.jpg" alt="Containers"><figcaption>Containers</figcaption></figure>
    <figure><img src="assets/eq-gaylord.jpg" alt="Gaylord box"><figcaption>Gaylord Box</figcaption></figure>
  </div>
  <p style="margin-top:28px"><a class="btn" href="contact.html">Ask about an equipment program</a></p>
</div></section>
"""

SERVICES = f"""
<section><div class="wrap">
  <img src="{IMAGES['services_hero']}" alt="Recycle icon on a wooden board on the grass" style="border-radius:14px;width:100%;max-height:380px;object-fit:cover">
  <div class="prose" style="margin-top:28px">
  <h1>Services</h1>
  <h3>At MPM, superior customer service is the name of the game.</h3>
  <p>We work daily with our customers to ensure that diligent and proper care is taken of their accounts. We closely monitor the recycling process so that everything runs smoothly and seamlessly. We want to make all your dealings with MPM helpful and pleasant.</p>
  <h2>MPM provides the following services</h2>
  <h3>Paper and Metal Waste Collection and Removal</h3>
  <p>MPM will analyze your particular needs and design a plan that best suits your company’s individual output. MPM will collect and remove your waste paper, aluminum plates and old inventory of paper – rolls and sheet fed materials. MPM will supply you with the appropriate containers; from Gaylord boxes and collapsible containers to black bin receptacles and spotted trailers which we drop directly at your facility. MPM’s Dispatch Division aims for same day service and guarantees pick-up no later than the next day. MPM’s experienced staff will leave your shop clean and organized without interrupting your day-to-day operations or production.</p>
  <h3>Recycling</h3>
  <p>For many customers, developing a cohesive and efficient recycling process ultimately results in smoother overall operations. At Marcells Paper &amp; Metal, we provide fast, professional and effective services that alleviate the stresses surrounding recycling and allow you to concentrate on your core business.</p>
  <p>MPM carefully grades and weighs collected waste at its state-of-the-art facility using a computerized scale system which meets the highest efficiency standards in the industry. Scrap is processed through our staging and sorting area where our staff carefully sorts the waste paper to eliminate contaminants. Waste is prepared for shipment by compacting and tying into neatly packed, mill specification bales. Bales are stored in our staging area – ready for mill shipment. MPM’s facility has immediate and adjacent rail service which makes moving waste across the country fast and convenient.</p>
  <h3>Secure Document Shredding</h3>
  <p>MPM offers professional and discreet collection of sensitive documents and files. MPM has added a dedicated site at our facility for the secure destruction of these materials.</p>
  <h3>Revenue &amp; Marketing</h3>
  <p>MPM receives and offers competitive pricing on recyclable waste – paying you top dollar. MPM’s relationships with both domestic and international mills allow us the flexibility to take advantage of movement and price. MPM’s Brokerage Division has the ability to move materials from anywhere across the country. For facilities with larger scale requirements, MPM offers recycling equipment to maximize your in-house capabilities — see our <a href="equipment.html">Equipment</a> page.</p>
  <h3>Marcells Pallet Inc</h3>
  <p>Our sister company builds, repairs and recycles pallets for the same customers — one pickup, one invoice, paper and pallets together.</p>
  <h3>Our experienced Customer Service Representatives will:</h3>
  <ul>
    <li><strong>Coordinate and schedule pick-ups:</strong> operating same day service on request before 10:00 am, including weekend pick-ups</li>
    <li><strong>Ensure that your facility is clean after pick-ups</strong></li>
    <li><strong>Record and enter all data once the waste has been brought back to MPM</strong></li>
    <li><strong>Process the payments back to the customer</strong></li>
    <li><strong>Have management maintain and review customer records to ensure that each customer gets the best return on their paper waste</strong></li>
  </ul>
  <p><a class="btn" href="contact.html">Request a quote</a></p>
  </div>
</div></section>
"""

METAL_WASTE = [
    ("p", "Marcells Paper and Metal INC is known as a reliable and professional recycling center in Chicago, IL. However, we don’t just accept cardboard, old documents, and other paper products — we also specialize in metal waste collection and removal! If you have aluminum plates and pans that you’d like to get rid of, just give us a call and we’ll collect it from your place."),
    ("h2", "Why Metal Should Be Recycled"),
    ("p", "A lot of people don’t really pay attention to their metal waste, which is why tons of metal items find their way to landfills every year. This is disheartening since most metal products can be recycled into usable products."),
    ("p", "One of the most commonly recycled metals is aluminum. Unlike other materials, aluminum doesn’t lose any of its intrinsic physical properties when it’s recycled. This means that virgin aluminum and recycled aluminum are virtually the same in structure and function and that it doesn’t require a lot of time, energy, and money to recycle aluminum products."),
    ("p", "By recycling your aluminum foil plates, trays, and pie pans, you can help reduce society’s reliance on bauxite ore (which is needed to produce aluminum). You can also help save a substantial amount of energy since the aluminum recycling process uses just 8 percent of the energy that’s needed to transform bauxite ore into usable aluminum."),
    ("h2", "Why Should You Choose Us?"),
    ("p", "We’re not the only recycling experts in Chicago, IL, so why should you decide to use our services? The answer is simple: we make metal recycling an easier and less stressful process for you!"),
    ("p", "We’ll supply you with containers of the appropriate sizes, and we’ll drop these containers right at your doorstep. Simply fill up these containers with all your metal (and paper!) items, and our staff will come back to collect them. We offer a same-day service, and we guarantee that the containers will be picked up no later than the next day. Of course, we don’t just retrieve your recyclable items; we’ll also ensure that your space is clean and organized after our pickup — without interrupting your operations!"),
    ("h2", "Contact Us Now"),
    ("p", f"Marcells Paper and Metal INC is the right company to trust if you’re searching for a dependable recycling center. Call us now at {PHONE_LINK} to use our metal waste collection and removal solutions in Chicago, IL!"),
]

PAPER_WASTE = [
    ("p", "Property owners in Chicago, IL know that they can rely on Marcells Paper and Metal INC when they need help with <a href=\"metal-recycling.html\">metal recycling</a>. However, we don’t just recycle metal items — we collect and remove paper waste, too! Call our team and use our paper waste collection and removal services today."),
    ("h2", "DIY Paper Waste Disposal: Is It a Good Idea?"),
    ("p", "Technically, you can opt to bring your paper waste to the nearest disposal facility all by yourself. However, before you begin, take note that this task isn’t as easy as it seems. Depending on where you live, you might need to obtain a permit from your local authorities before you can handle, recycle, and dispose of paper waste. You should also secure a vehicle that’s large enough to accommodate the amount of paper waste that you’d like to dispose of. Of course, you need to know the proper way of handling paper waste. Otherwise, you can end up contaminating recyclable items and make them unfit for recycling."),
    ("p", "If you don’t have the time or energy to tackle these tasks, it’s best to get our help. With our expertise in waste collection and recycling, we can help you dispose of your paper waste in a fast, efficient and hassle-free way."),
    ("h2", "What We Collect"),
    ("p", "We can collect your old inventory of paper, both individual sheets for sheet-fed printing and rolls of paper for web printing. We also take used paper that’s ready for disposal. We will provide you with the appropriate containers, so the only thing you should do is fill these containers with your paper waste. Once you’re done, just call us and we’ll retrieve your waste materials within the shortest possible time."),
    ("h2", "Get in Touch With Us"),
    ("p", f"When it comes to paper waste collection and removal, Marcells Paper and Metal INC is one of the best experts that you can trust in Chicago, IL. Dial {PHONE_LINK} now to schedule an appointment with us. You can also give us a ring to use our dependable metal recycling, collection, and removal services."),
]

METAL_RECYCLING = [
    ("p", "Any construction project, regardless of size, produces quantities of metal waste. You can clean up the rest of your construction clutter and debris but metal is an entirely different matter. There are certain state laws and regulations that should be followed when disposing of or handling metal waste. You can’t just dump the metal waste at your nearest landfill. Metal needs to be handled by professionals who can recycle it and make use of it in other projects. You can trust a recycling center like Marcells Paper and Metal INC to handle your metal waste collection and recycling needs. To learn more about the services we provide to residential and commercial property owners in Chicago, IL, read on."),
    ("h2", "We Are Committed"),
    ("p", "As a committed recycling center, we understand that every business requires a recycling solution that fits seamlessly and so we make sure to take care of our clients’ needs in a professional, personal and efficient manner. We offer the flexibility of a local independent business to meet the unique needs of every client. You can count on our services all the time as we pride ourselves on our extensive knowledge of various industries. We are a premier recycler of scrap metal products and equipped with the processes, sorting and marketing capabilities."),
    ("h2", "We Value Our Clients"),
    ("p", "On top of our competitive prices, we also offer friendly service. We demonstrate professionalism as we maintain excellent professional relationships with our clients. To make sure all of your metal recycling needs are met, we suggest ways to up your recycling game and reduce your costs. It is our goal to provide you the maximum value for your recyclable commodities for increased profitability. You are encouraged to make an eco-friendly choice as we help you find markets for products that are hard to move and also for you to dispose of your waste in an eco-friendly manner."),
    ("p", f"Let Marcells Paper and Metal INC take care of your metal waste collection and recycling needs. Call us today at {PHONE_LINK} to inquire about our services offered in Chicago, IL."),
]

PAPER_RECYCLING = [
    ("p", "MPM excels at assisting clients with smooth and efficient fulfillment and paper waste removal and recycling. We work with a broad spectrum of paper grades — from newspaper and corrugated to high grade and pulp substitutes — and our direct relationships with the paper mills allow us to work on our clients’ best behalf and generate top value for your paper waste."),
    ("h2", "What happens to your paper"),
    ("p", "Collected paper is graded and weighed at our facility on a computerized scale system, sorted to remove contaminants, then compacted and tied into mill-specification bales. Our facility has immediate, adjacent rail service, so material moves to mills across the country quickly and at the best available price."),
    ("h2", "Grades we buy"),
    ("ul", ["Printers mix, sorted and mixed white ledger, colored ledger and envelope cuttings",
            "Coated and uncoated book stock, news blanks and publication blanks",
            "Old corrugated containers (OCC), double-lined kraft (DLK) and boxboard",
            "Old newspaper, magazines and groundwood grades",
            "Hard white, soft white and other pulp substitutes",
            "New and job-lot paper inventory — cut sheets and rolls"]),
    ("h2", "Secure document destruction"),
    ("p", "Sensitive files are collected discreetly and destroyed at a dedicated, isolated site inside our facility under 24-hour video surveillance with remote viewing access."),
    ("p", f"<strong>Please call us for a free consultation and quote at {PHONE_LINK}. No job is too big!</strong>"),
]

CONTACT = f"""
<section><div class="wrap">
  <div class="prose"><h1>Contact</h1>
  <h3>Marcells Paper &amp; Metal happily welcomes all inquiries.</h3>
  <p>Please feel free to contact us with questions and we will do our best to provide you with timely answers.</p></div>
  <div class="contact-grid" style="margin-top:24px">
    <div>
      <h3 style="margin-top:0">General Inquiries</h3>
      <form action="mailto:info@marcellspaper.com" method="post" enctype="text/plain" onsubmit="return sendMail(this)">
        <label for="name">Name</label><input id="name" name="Name" required>
        <label for="email">Email Address *</label><input id="email" name="Email" type="email" required>
        <label for="phone">Phone</label><input id="phone" name="Phone">
        <label for="topic">I&#39;m asking about</label>
        <select id="topic" name="Topic"><option>General quote</option><option>Paper quote</option><option>Metal quote</option><option>Scheduling a pickup</option><option>Equipment</option><option>Something else</option></select>
        <label for="msg">Message</label><textarea id="msg" name="Message" rows="5"></textarea>
        <button class="btn" type="submit">Send</button>
        <p style="font-size:13px;color:var(--muted)">Opens a pre-filled email to info@marcellspaper.com from your mail app. Or just call us — it&#39;s faster.</p>
      </form>
      <script>
      function sendMail(f){{var b='Name: '+f.Name.value+'\\nEmail: '+f.Email.value+'\\nPhone: '+f.Phone.value+'\\nAbout: '+f.Topic.value+'\\n\\n'+f.Message.value;
        window.location.href='mailto:info@marcellspaper.com?subject='+encodeURIComponent(f.Topic.value+' - '+f.Name.value)+'&body='+encodeURIComponent(b);return false;}}
      </script>
    </div>
    <div>
      <h3 style="margin-top:0">Marcells Paper &amp; Metal</h3>
      <p><strong>Phone:</strong> {PHONE_LINK}<br><strong>Fax:</strong> (773) 265-1220<br><strong>Email:</strong> <a href="mailto:info@marcellspaper.com">info@marcellspaper.com</a><br><strong>Address:</strong> 4221 W Ferdinand St., Chicago, Illinois 60624</p>
      <p><a class="btn ghost" href="https://www.google.com/maps/search/?api=1&query=4221+W+Ferdinand+St+Chicago+IL+60624" target="_blank" rel="noopener">Get directions</a></p>
      <h3>Choose an option</h3>
      <div class="quotes">
        <a href="mailto:info@marcellspaper.com?subject=General%20Quote">General Quote</a>
        <a href="mailto:info@marcellspaper.com?subject=Paper%20Quote">Paper Quote</a>
        <a href="mailto:info@marcellspaper.com?subject=Metal%20Quote">Metal Quote</a>
      </div>
      <h3>Already a customer?</h3>
      <p>Track your loads, statements and pricing on the <a href="https://portal.marcellspaper.com" target="_blank" rel="noopener">customer portal</a>.</p>
    </div>
  </div>
</div></section>
"""

FAQ_ITEMS = [
    ("How does MPM provide consistent pricing for my scrap when the market is always changing?", "Our relationships with both domestic and international mills give us the flexibility to take advantage of movement and price."),
    ("What types of materials do you take?", "MPM takes all grades of paper, aluminum plates and all plastics."),
    ("Does MPM buy old paper inventory?", "Yes! MPM buys both sheet-fed materials and rolls."),
    ("Does MPM service accounts outside of Illinois?", "Yes we do. MPM services accounts from San Diego to Boston."),
    ("How often do you pick up, and do you operate on weekends?", "MPM operates 6 days a week and can arrange for Sunday pick-ups if requested. We schedule pick-ups to meet the needs of our customers. Special pick-ups can be dispatched within 24 hours by our Customer Service department."),
    ("Will the price I receive for my waste fluctuate?", "Waste paper is a commodity and pricing will vary from time to time based on the amount of waste paper on the market at any given time."),
    ("Do you supply the containers for my waste?", "Yes, MPM provides a full range of containers from gaylord boxes and collapsible containers to black bin receptacles and spotted trailers dropped at your facility. We supply what you need."),
]
FAQ = '<section><div class="wrap"><div class="prose"><h1>Frequently Asked Questions</h1><div class="faq">' + "".join(
    f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ_ITEMS) + f'</div><p style="margin-top:24px">Still have a question? Call {PHONE_LINK} or <a href="contact.html">send us a message</a>.</p></div></div></section>'

PAGES = {
    "index": {"title": "Marcells Paper & Metal | Paper & Metal Recycling, Chicago IL", "desc": "Marcells Paper & Metal offers efficient paper and metal recovery services in Chicago — pickup, containers, secure document destruction and top-dollar pricing. Call (773) 265-1200.", "body": HOME},
    "about": {"title": "About Us | Marcells Paper & Metal", "desc": "How Scott Lowell turned a trunk full of computer punch cards into Marcells Paper & Metal, Chicago's family-owned paper and metal recycling center.", "h1": "Marcells Paper and Metal", "blocks": ABOUT},
    "equipment": {"title": "Recycling Equipment | Marcells Paper & Metal", "desc": "Balers, conveyors and containers sized to your tonnage — with financing, installation, waste removal and ongoing support from Marcells Paper & Metal.", "body": EQUIPMENT},
    "services": {"title": "Recycling Services | Marcells Paper & Metal", "desc": "Paper and metal waste collection, recycling, secure document shredding, brokerage and customer service from Marcells Paper & Metal in Chicago.", "body": SERVICES},
    "metal-waste-collection": {"title": "Metal Waste Collection | Marcells Paper & Metal", "desc": "Metal waste collection and removal in Chicago, IL — aluminum plates, pans and more, with containers dropped at your door and same-day pickup.", "h1": "Metal Waste Collection and Removal", "blocks": METAL_WASTE},
    "paper-waste-collection": {"title": "Paper Waste Collection | Marcells Paper & Metal", "desc": "Paper waste collection and removal in Chicago, IL — old inventory, sheets, rolls and used paper, containers supplied, fast pickup.", "h1": "Beyond Metal Recycling: We Can Also Collect and Remove Your Paper Waste!", "blocks": PAPER_WASTE},
    "metal-recycling": {"title": "Metal Recycling | Marcells Paper & Metal", "desc": "A reliable recycling center for your metal waste collection and recycling needs in Chicago, IL.", "h1": "The Reliable Recycling Center for Your Metal Waste Collection and Recycling Needs", "blocks": METAL_RECYCLING},
    "paper-recycling": {"title": "Paper Recycling | Marcells Paper & Metal", "desc": "Paper recycling in Chicago — every grade from OCC and news to high grades and pulp substitutes, baled to mill spec and shipped by rail. Free quote.", "h1": "Paper Recycling", "blocks": PAPER_RECYCLING},
    "contact": {"title": "Contact Us | Marcells Paper & Metal", "desc": "Contact Marcells Paper & Metal — (773) 265-1200, 4221 W Ferdinand St, Chicago, IL 60624. Request a general, paper or metal quote.", "body": CONTACT},
    "faq": {"title": "Scrap Recycling FAQ | Marcells Paper & Metal", "desc": "Answers about pricing, materials we take, old paper inventory, pickups, weekends and containers.", "body": FAQ},
}
