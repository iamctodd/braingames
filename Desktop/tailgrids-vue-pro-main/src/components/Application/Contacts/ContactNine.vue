<template>
  <!-- ====== Contact Section Start -->
  <section class="bg-primary relative z-10 py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div class="bg-white dark:bg-dark-2">
        <div class="flex flex-wrap items-stretch">
          <div class="w-full lg:w-7/12">
            <div class="relative flex w-full h-full overflow-hidden">
              <div class="flex items-end h-full">
                <img
                  src="https://cdn.tailgrids.com/2.0/image/application/images/contact/contact-image-9.jpg"
                  alt="image"
                  class="object-cover object-center w-full h-full"
                />
              </div>
              <div class="absolute bottom-14 left-0 right-0 mx-auto w-full max-w-[560px] px-5">
                <div
                  class="flex-wrap items-center w-full px-4 bg-white rounded dark:bg-dark-2 shadow-[0px_4px_10px_0px_rgba(0,0,0,0.25)] py-9 md:inline-flex md:px-4 lg:px-0 xl:px-4"
                >
                  <div class="px-3 mb-4 border-stroke dark:border-dark-3 md:mb-0 md:border-r">
                    <h5 class="text-lg font-semibold text-dark dark:text-white">Email</h5>
                    <p class="text-base dark:text-dark-6 text-body-color">info@example.com</p>
                  </div>
                  <div class="px-3 mb-4 border-stroke dark:border-dark-3 md:mb-0 md:border-r">
                    <h5 class="text-lg font-semibold text-dark dark:text-white">Phone</h5>
                    <p class="text-base dark:text-dark-6 text-body-color">+99 021 324 258</p>
                  </div>
                  <div class="px-3">
                    <h5 class="text-lg font-semibold text-dark dark:text-white">Address</h5>
                    <p class="text-base dark:text-dark-6 text-body-color">340 Main St, USA</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="w-full lg:w-5/12">
            <div class="2xl:px-70 w-full py-14 px-8 sm:p-[70px] lg:px-14">
              <span class="block mb-5 text-base font-medium text-dark dark:text-white">
                CONTACT US
              </span>
              <h2
                class="text-3xl font-semibold leading-tight text-dark dark:text-white mb-9 sm:text-4xl sm:leading-tight"
              >
                Let's talk about <br />
                your problem.
              </h2>
              <form>
                <div class="mb-5">
                  <label
                    for=""
                    class="block mb-2.5 text-base font-medium text-dark dark:text-white"
                  >
                    Your Name
                  </label>
                  <input
                    type="text"
                    placeholder="Enter your name"
                    class="w-full px-5 py-3 text-base bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 dark:text-dark-6 text-body-color focus:border-primary focus-visible:shadow-none"
                  />
                </div>
                <div class="mb-5">
                  <label
                    for=""
                    class="block mb-2.5 text-base font-medium text-dark dark:text-white"
                  >
                    Your Email
                  </label>
                  <input
                    type="email"
                    placeholder="Enter your email"
                    class="w-full px-5 py-3 text-base bg-transparent border rounded-md outline-none border-stroke dark:border-dark-3 dark:text-dark-6 text-body-color focus:border-primary focus-visible:shadow-none"
                  />
                </div>
                <div class="mb-8">
                  <label
                    for=""
                    class="block mb-2.5 text-base font-medium text-dark dark:text-white"
                  >
                    Your Message
                  </label>
                  <textarea
                    rows="5"
                    placeholder="Enter your email"
                    class="w-full px-5 py-3 text-base bg-transparent border rounded-md outline-none resize-none border-stroke dark:border-dark-3 dark:text-dark-6 text-body-color focus:border-primary focus-visible:shadow-none"
                  ></textarea>
                </div>
                <div>
                  <button
                    type="submit"
                    class="py-3 text-white transition border border-transparent rounded-md cursor-pointer px-7 bg-primary hover:bg-opacity-90"
                  >
                    Send Message
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Contact Section End -->
</template>
