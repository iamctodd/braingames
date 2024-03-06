<template>
  <!-- ====== Contact Section Start -->
  <section class="py-24 overflow-hidden bg-white dark:bg-dark">
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <div class="w-full px-4">
          <div class="mx-auto mb-[60px] max-w-[770px] text-center">
            <h2
              class="mb-3 text-center text-3xl font-bold leading-tight text-dark dark:text-white md:text-4xl md:leading-tight xl:text-[45px] xl:leading-tight"
            >
              Need Help? Open a Ticket
            </h2>
            <p
              class="text-base leading-relaxed text-body-color dark:text-dark-6 md:text-lg md:leading-relaxed"
            >
              Submit Your Support Ticket, We will be with you as soon as we are able.
            </p>
          </div>
        </div>
      </div>
      <div class="flex -mx-4">
        <div class="w-full px-4">
          <div
            class="border-form-stroke shadow-[0px_0px_40px_0px_rgba(0,0,0,0.05)] relative mx-auto w-full max-w-[770px] border bg-white py-10 px-6 sm:py-[60px] sm:px-[65px] md:p-10 lg:py-[60px] dark:bg-dark-2 dark:border-dark-3 lg:px-[65px]"
          >
            <form>
              <div class="flex flex-wrap -mx-4">
                <div class="w-full px-4 md:w-1/2">
                  <div class="mb-7">
                    <label
                      for="firstName"
                      class="block mb-2.5 text-base font-medium text-dark dark:text-white"
                    >
                      First Name
                    </label>
                    <input
                      id="firstName"
                      type="text"
                      name="firstName"
                      placeholder="Enter your first name"
                      class="w-full px-6 py-4 bg-transparent border outline-none placeholder-secondary-color border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 focus:border-primary"
                    />
                  </div>
                </div>
                <div class="w-full px-4 md:w-1/2">
                  <div class="mb-7">
                    <label
                      for="lastName"
                      class="block mb-2.5 text-base font-medium text-dark dark:text-white"
                    >
                      Last Name
                    </label>
                    <input
                      id="lastName"
                      type="text"
                      name="lastName"
                      placeholder="Enter your last Name"
                      class="w-full px-6 py-4 bg-transparent border outline-none placeholder-secondary-color border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 focus:border-primary"
                    />
                  </div>
                </div>
                <div class="w-full px-4 md:w-1/2">
                  <div class="mb-7">
                    <label
                      for="email"
                      class="block mb-2.5 text-base font-medium text-dark dark:text-white"
                    >
                      Business Email
                    </label>
                    <input
                      id="email"
                      type="email"
                      name="email"
                      placeholder="Enter your Email"
                      class="w-full px-6 py-4 bg-transparent border outline-none placeholder-secondary-color border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 focus:border-primary"
                    />
                  </div>
                </div>
                <div class="w-full px-4 md:w-1/2">
                  <div class="mb-7">
                    <label
                      for="number"
                      class="block mb-2.5 text-base font-medium text-dark dark:text-white"
                    >
                      Phone number
                    </label>
                    <input
                      id="number"
                      type="text"
                      name="number"
                      placeholder="Enter your number"
                      class="w-full px-6 py-4 bg-transparent border outline-none placeholder-secondary-color border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 focus:border-primary"
                    />
                  </div>
                </div>
                <div class="w-full px-4">
                  <div class="mb-7">
                    <label
                      for="message"
                      class="block mb-2.5 text-base font-medium text-dark dark:text-white"
                    >
                      What are you looking for?
                    </label>
                    <textarea
                      id="message"
                      name="message"
                      placeholder="Type your message here"
                      rows="6"
                      class="w-full px-6 py-4 bg-transparent border outline-none resize-none placeholder-secondary-color border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 focus:border-primary"
                    ></textarea>
                  </div>
                </div>
                <div class="w-full px-4">
                  <div class="text-center">
                    <button
                      type="submit"
                      class="inline-flex items-center justify-center py-3 text-base font-medium text-white border border-transparent px-7 bg-primary hover:bg-opacity-90"
                    >
                      Submit Ticket
                    </button>
                  </div>
                </div>
              </div>
            </form>
            <div>
              <span class="absolute -top-5 -right-5 -z-10">
                <svg
                  width="57"
                  height="121"
                  viewBox="0 0 57 121"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <circle cx="23.0992" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="118.746" r="1.62854" fill="#3056D3" />
                </svg>
              </span>
              <span class="absolute -bottom-5 -left-5 -z-10">
                <svg
                  width="57"
                  height="121"
                  viewBox="0 0 57 121"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <circle cx="23.0992" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3649" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="23.0992" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="12.3629" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="1.62854" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="33.8571" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="44.6149" cy="118.746" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="1.62854" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="12.3864" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="23.1422" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="33.9005" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="44.6515" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="55.4049" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="66.1559" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="76.6744" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="87.193" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="97.7111" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="108.227" r="1.62854" fill="#3056D3" />
                  <circle cx="55.3707" cy="118.746" r="1.62854" fill="#3056D3" />
                </svg>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Contact Section End -->
</template>
