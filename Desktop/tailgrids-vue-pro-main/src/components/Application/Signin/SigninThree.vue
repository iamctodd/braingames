<template>
  <!-- ====== Forms Section Start -->
  <section class="relative z-10 bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="absolute left-0 top-0 z-[-1] h-full w-1/4 bg-primary"></div>
    <div class="container mx-auto">
      <div class="bg-white dark:bg-dark-2">
        <div class="flex flex-wrap items-stretch">
          <div class="w-full lg:w-1/2">
            <div class="relative hidden w-full h-full overflow-hidden lg:flex">
              <div class="flex items-end h-full">
                <img
                  src="https://cdn.tailgrids.com/2.0/image/application/images/forms/image-01.jpg"
                  alt="image"
                  class="object-cover object-center w-full h-full"
                />
              </div>
            </div>
          </div>
          <div class="w-full lg:w-1/2">
            <div class="w-full py-14 px-8 sm:p-[70px] lg:px-14 xl:px-[90px]">
              <h2 class="mb-3 text-3xl font-bold dark:text-white text-dark">
                Welcome to TailGrids
              </h2>
              <p class="text-base mb-14 text-secondary-color dark:text-dark-7 xl:mb-20">
                <span class="sm:block"> We make it easy for everyone to </span>
                <span>access their account</span>
              </p>
              <form>
                <div class="mb-6">
                  <input
                    type="email"
                    placeholder="Enter your email"
                    class="w-full h-12 px-5 bg-transparent border border-transparent outline-none text-body-color focus:border-primary focus-visible:shadow-none dark:border-dark-3 bg-gray-2 dark:bg-dark dark:text-white"
                  />
                </div>
                <div class="mb-8">
                  <input
                    type="password"
                    placeholder="Enter your Password"
                    class="w-full h-12 px-5 bg-transparent border border-transparent outline-none text-body-color focus:border-primary focus-visible:shadow-none dark:border-dark-3 bg-gray-2 dark:bg-dark dark:text-white"
                  />
                </div>
                <div class="flex flex-wrap justify-between mb-8">
                  <div class="mb-2 mr-2">
                    <label
                      for="checkboxLabelTwo"
                      class="flex items-center text-base cursor-pointer text-body-color dark:text-dark-6"
                    >
                      <div class="relative">
                        <input type="checkbox" id="checkboxLabelTwo" class="sr-only" />
                        <div
                          class="flex items-center justify-center w-5 h-5 mr-3 border rounded box border-stroke dark:border-dark-3"
                        >
                          <span class="opacity-0">
                            <svg
                              width="11"
                              height="8"
                              viewBox="0 0 11 8"
                              fill="none"
                              xmlns="http://www.w3.org/2000/svg"
                            >
                              <path
                                d="M10.0915 0.951972L10.0867 0.946075L10.0813 0.940568C9.90076 0.753564 9.61034 0.753146 9.42927 0.939309L4.16201 6.22962L1.58507 3.63469C1.40401 3.44841 1.11351 3.44879 0.932892 3.63584C0.755703 3.81933 0.755703 4.10875 0.932892 4.29224L0.932878 4.29225L0.934851 4.29424L3.58046 6.95832C3.73676 7.11955 3.94983 7.2 4.1473 7.2C4.36196 7.2 4.55963 7.11773 4.71406 6.9584L10.0468 1.60234C10.2436 1.4199 10.2421 1.1339 10.0915 0.951972ZM4.2327 6.30081L4.2317 6.2998C4.23206 6.30015 4.23237 6.30049 4.23269 6.30082L4.2327 6.30081Z"
                                fill="#3056D3"
                                stroke="#3056D3"
                                stroke-width="0.4"
                              />
                            </svg>
                          </span>
                        </div>
                      </div>
                      Remember Me
                    </label>
                  </div>
                  <a href="javascript:void(0)" class="mb-2 text-base text-primary hover:underline">
                    Forget Password?
                  </a>
                </div>
                <div class="flex flex-wrap -mx-3">
                  <div class="w-full px-3 md:w-1/2">
                    <button
                      type="submit"
                      class="mb-3 h-[50px] w-full cursor-pointer bg-primary px-5 text-white transition hover:bg-opacity-90 font-medium"
                    >
                      Sign In
                    </button>
                  </div>
                  <div class="w-full px-3 md:w-1/2">
                    <button
                      class="mb-3 h-[50px] w-full cursor-pointer bg-secondary px-5 text-white transition hover:bg-opacity-90 font-medium"
                    >
                      Create Account
                    </button>
                  </div>
                </div>
              </form>
              <div class="flex flex-wrap items-center mt-6 md:mt-10">
                <p class="mb-3 mr-5 text-xs font-medium text-body-color dark:text-dark-6">
                  Login With
                </p>
                <div class="flex items-center mb-3">
                  <a
                    href="javascript:void(0)"
                    class="mr-4 text-xs font-medium text-dark dark:text-white hover:text-primary hover:underline"
                  >
                    Facebook
                  </a>
                  <a
                    href="javascript:void(0)"
                    class="mr-4 text-xs font-medium text-dark dark:text-white hover:text-primary hover:underline"
                  >
                    Twitter
                  </a>
                  <a
                    href="javascript:void(0)"
                    class="mr-4 text-xs font-medium text-dark dark:text-white hover:text-primary hover:underline"
                  >
                    Google
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Forms Section End -->
</template>
