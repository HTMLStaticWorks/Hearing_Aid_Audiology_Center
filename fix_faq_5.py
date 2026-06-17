import sys

file_path = r'e:\OfficeDownloads_\MayJuneWebsite\Hearing_Aid_Audiology_Center\faq.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = '<!-- FAQ Section Grid -->'
end_tag = '<!-- Still Have Questions Callout -->'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag)

if start_idx != -1 and end_idx != -1:
    new_grid = """<!-- FAQ Section Grid -->
    <section class="py-5 bg-light">
      <div class="container">
        <div class="row g-4 justify-content-center">
          
          <!-- Section 1: Clinic & Appointments -->
          <div class="col-lg-6">
            <div class="card glass p-4 border-0 shadow-sm h-100 mb-4">
              <img src="assets/images/clinic_reception.png" alt="Clinic & Appointments" class="rounded-3 mb-4 w-100" style="height: 200px; object-fit: cover;">
              <div class="d-flex align-items-center gap-3 mb-4">
                <div class="bg-primary text-white rounded-3 p-2 d-flex align-items-center justify-content-center" style="width: 42px; height: 42px;">
                  <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
                    <line x1="16" y1="2" x2="16" y2="6" />
                    <line x1="8" y1="2" x2="8" y2="6" />
                    <line x1="3" y1="10" x2="21" y2="10" />
                  </svg>
                </div>
                <h2 class="h4 fw-bold mb-0">Clinic & Appointments</h2>
              </div>
              <div class="accordion" id="faqAccordion1">
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading1-1">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-1" aria-expanded="false" aria-controls="collapse1-1">
                      How do I schedule an appointment at Sono?
                    </button>
                  </h3>
                  <div id="collapse1-1" class="accordion-collapse collapse" aria-labelledby="heading1-1" data-bs-parent="#faqAccordion1">
                    <div class="accordion-body">
                      You can schedule a visit by clicking any "Book Now" or "Book Appointment" button on our website, filling out our contact form, or calling our direct support line at (555) 123-4567. We offer both initial clinical evaluations and follow-up adjustments.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading1-2">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-2" aria-expanded="false" aria-controls="collapse1-2">
                      What are your operating hours and location?
                    </button>
                  </h3>
                  <div id="collapse1-2" class="accordion-collapse collapse" aria-labelledby="heading1-2" data-bs-parent="#faqAccordion1">
                    <div class="accordion-body">
                      Our clinic is open Monday through Friday, from 9:00 AM to 5:00 PM. We are located at 123 Hearing Health Way, Hearingville, CA. Complimentarty parking is available for all patients in the private front lot.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading1-3">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-3" aria-expanded="false" aria-controls="collapse1-3">
                      Do I need a doctor's referral to visit your center?
                    </button>
                  </h3>
                  <div id="collapse1-3" class="accordion-collapse collapse" aria-labelledby="heading1-3" data-bs-parent="#faqAccordion1">
                    <div class="accordion-body">
                      No, a doctor's referral is not required to schedule a diagnostic evaluation or consulting session with our audiology specialists. However, if your insurance policy mandates a referral for diagnostic benefits, please confirm prior to booking.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 2: Hearing Diagnostics & Tests -->
          <div class="col-lg-6">
            <div class="card glass p-4 border-0 shadow-sm h-100 mb-4">
              <img src="assets/images/hearing_test.png" alt="Hearing Diagnostics" class="rounded-3 mb-4 w-100" style="height: 200px; object-fit: cover;">
              <div class="d-flex align-items-center gap-3 mb-4">
                <div class="bg-primary text-white rounded-3 p-2 d-flex align-items-center justify-content-center" style="width: 42px; height: 42px;">
                  <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                  </svg>
                </div>
                <h2 class="h4 fw-bold mb-0">Hearing Diagnostics</h2>
              </div>
              <div class="accordion" id="faqAccordion2">
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading2-1">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse2-1" aria-expanded="false" aria-controls="collapse2-1">
                      What happens during a comprehensive hearing test?
                    </button>
                  </h3>
                  <div id="collapse2-1" class="accordion-collapse collapse" aria-labelledby="heading2-1" data-bs-parent="#faqAccordion2">
                    <div class="accordion-body">
                      A standard evaluation takes about 30 to 45 minutes. Our certified specialist performs an otoscopic ear exam to check the canal and eardrum. Then, you'll enter a soundproof booth to listen to varying pure-tone frequencies and speech tests through custom headphones.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading2-2">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse2-2" aria-expanded="false" aria-controls="collapse2-2">
                      How frequently should I schedule a hearing test?
                    </button>
                  </h3>
                  <div id="collapse2-2" class="accordion-collapse collapse" aria-labelledby="heading2-2" data-bs-parent="#faqAccordion2">
                    <div class="accordion-body">
                      We recommend that adults aged 50 and above undergo screening every two years, or annually if they are frequently exposed to loud noise. If you experience symptoms like ringing in the ears or struggle to follow group discussions, please book immediately.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading2-3">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse2-3" aria-expanded="false" aria-controls="collapse2-3">
                      Is the audiology test painful or uncomfortable?
                    </button>
                  </h3>
                  <div id="collapse2-3" class="accordion-collapse collapse" aria-labelledby="heading2-3" data-bs-parent="#faqAccordion2">
                    <div class="accordion-body">
                      No. Diagnostic hearing tests are completely painless and non-invasive. You simply respond to the quietest sounds you can hear by raising your hand or pressing a button.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 3: Hearing Aid Technology -->
          <div class="col-lg-6">
            <div class="card glass p-4 border-0 shadow-sm h-100 mb-4">
              <img src="assets/images/hearing_technology.png" alt="Hearing Aid Technology" class="rounded-3 mb-4 w-100" style="height: 200px; object-fit: cover;">
              <div class="d-flex align-items-center gap-3 mb-4">
                <div class="bg-primary text-white rounded-3 p-2 d-flex align-items-center justify-content-center" style="width: 42px; height: 42px;">
                  <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M6 8.5a6.5 6.5 0 1 1 13 0c0 6-6 6-6 10a3.5 3.5 0 1 1-7 0" />
                    <path d="M15 8.5a2.5 2.5 0 0 0-5 0v2" />
                  </svg>
                </div>
                <h2 class="h4 fw-bold mb-0">Hearing Aid Technology</h2>
              </div>
              <div class="accordion" id="faqAccordion3">
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading3-1">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse3-1" aria-expanded="false" aria-controls="collapse3-1">
                      What styles of hearing aids do you custom-fit?
                    </button>
                  </h3>
                  <div id="collapse3-1" class="accordion-collapse collapse" aria-labelledby="heading3-1" data-bs-parent="#faqAccordion3">
                    <div class="accordion-body">
                      We offer a diverse selection of models, including Receiver-in-Canal (RIC), Behind-the-Ear (BTE), In-the-Ear (ITE), and custom, ultra-discreet Completely-in-Canal (CIC) or Invisible-in-Canal (IIC) options that sit completely unseen.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading3-2">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse3-2" aria-expanded="false" aria-controls="collapse3-2">
                      Can I stream audio directly to my hearing aids?
                    </button>
                  </h3>
                  <div id="collapse3-2" class="accordion-collapse collapse" aria-labelledby="heading3-2" data-bs-parent="#faqAccordion3">
                    <div class="accordion-body">
                      Yes. Most of our modern digital hearing aids feature Bluetooth LE connectivity, allowing you to stream phone calls, music, podcasts, and television audio directly from Apple iOS and Android devices.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading3-3">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse3-3" aria-expanded="false" aria-controls="collapse3-3">
                      How long do rechargeable hearing aid batteries last?
                    </button>
                  </h3>
                  <div id="collapse3-3" class="accordion-collapse collapse" aria-labelledby="heading3-3" data-bs-parent="#faqAccordion3">
                    <div class="accordion-body">
                      Modern rechargeable lithium-ion hearing devices typically run for 20 to 24 hours on a single 3-hour charge, even when utilizing streaming features. The protective cases also serve as portable chargers for weekend trips.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 4: Pricing, Insurance & Tinnitus Care -->
          <div class="col-lg-6">
            <div class="card glass p-4 border-0 shadow-sm h-100 mb-4">
              <img src="assets/images/patient_consultation.png" alt="Pricing & Special Services" class="rounded-3 mb-4 w-100" style="height: 200px; object-fit: cover;">
              <div class="d-flex align-items-center gap-3 mb-4">
                <div class="bg-primary text-white rounded-3 p-2 d-flex align-items-center justify-content-center" style="width: 42px; height: 42px;">
                  <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="10" />
                    <path d="M12 6v6l4 2" />
                  </svg>
                </div>
                <h2 class="h4 fw-bold mb-0">Pricing & Special Services</h2>
              </div>
              <div class="accordion" id="faqAccordion4">
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading4-1">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse4-1" aria-expanded="false" aria-controls="collapse4-1">
                      Do you accept major health insurance plans?
                    </button>
                  </h3>
                  <div id="collapse4-1" class="accordion-collapse collapse" aria-labelledby="heading4-1" data-bs-parent="#faqAccordion4">
                    <div class="accordion-body">
                      Yes, we partner with major insurance providers. Hearing aid coverage details differ heavily depending on your employer group or individual plan. Our billing specialists can submit inquiries and verify your benefits prior to your trial.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading4-2">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse4-2" aria-expanded="false" aria-controls="collapse4-2">
                      What is your trial and return policy for hearing aids?
                    </button>
                  </h3>
                  <div id="collapse4-2" class="accordion-collapse collapse" aria-labelledby="heading4-2" data-bs-parent="#faqAccordion4">
                    <div class="accordion-body">
                      We offer a risk-free 45-day adaptation trial period for all customized hearing aids. If you do not experience a significant increase in sound comfort and communication clarity, you can return them for a full refund or choose a different model.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading4-3">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse4-3" aria-expanded="false" aria-controls="collapse4-3">
                      How does your tinnitus treatment program work?
                    </button>
                  </h3>
                  <div id="collapse4-3" class="accordion-collapse collapse" aria-labelledby="heading4-3" data-bs-parent="#faqAccordion4">
                    <div class="accordion-body">
                      We offer custom sound therapy strategies. This includes fitting specialized hearing devices that emit customized static or ocean-wave maskers to desensitize the brain, combined with clinical cognitive counseling.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 5: Aftercare & Support (Centered) -->
          <div class="col-lg-6">
            <div class="card glass p-4 border-0 shadow-sm h-100 mb-4">
              <img src="assets/images/ear_protection.png" alt="Aftercare & Support" class="rounded-3 mb-4 w-100" style="height: 200px; object-fit: cover;">
              <div class="d-flex align-items-center gap-3 mb-4">
                <div class="bg-primary text-white rounded-3 p-2 d-flex align-items-center justify-content-center" style="width: 42px; height: 42px;">
                  <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                  </svg>
                </div>
                <h2 class="h4 fw-bold mb-0">Aftercare & Support</h2>
              </div>
              <div class="accordion" id="faqAccordion5">
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading5-1">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse5-1" aria-expanded="false" aria-controls="collapse5-1">
                      How do I clean and maintain my hearing aids?
                    </button>
                  </h3>
                  <div id="collapse5-1" class="accordion-collapse collapse" aria-labelledby="heading5-1" data-bs-parent="#faqAccordion5">
                    <div class="accordion-body">
                      We provide a detailed cleaning kit and instructions with every fitting. Generally, you should wipe them daily with a dry cloth, use a brush to remove wax, and avoid exposing them to excessive moisture.
                    </div>
                  </div>
                </div>
                <div class="accordion-item">
                  <h3 class="accordion-header" id="heading5-2">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse5-2" aria-expanded="false" aria-controls="collapse5-2">
                      What if my hearing changes after I purchase my devices?
                    </button>
                  </h3>
                  <div id="collapse5-2" class="accordion-collapse collapse" aria-labelledby="heading5-2" data-bs-parent="#faqAccordion5">
                    <div class="accordion-body">
                      We offer free reprogramming and adjustments within the first year. Your hearing aids can be fine-tuned to match any changes in your hearing profile over time.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
    """
    
    content = content[:start_idx] + new_grid + "\n" + content[end_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done!")
else:
    print("Could not find start or end tags.")
