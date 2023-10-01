<script setup lang="ts">
const route = useRoute();

const page = computed(() => {
  
  const fullPath = route.fullPath || '';
  console.log(fullPath);

  const pageData = {
    "sign-in": {
      label: "pages.auth.sign-in.index.sign-up",
      message: "pages.auth.sign-in.index.welcome-back",
      // icon: "noto-v1:waving-hand",
      icon:"",
      title: "pages.auth.sign-in.index.title",
      link: "/auth/sign-up",
    },
    "sign-up": {
      label: "pages.auth.sign-up.index.sign-in",
      message: "pages.auth.sign-up.index.first-time-welcome",
      // icon: "noto-v1:raised-fist",
      icon: "",
      title: "pages.auth.sign-up.index.title",
      link: "/auth/sign-in",
    },
    default: {
      label: "",
      message: "",
      icon: "",
      title: "",
    },
  };

  return pageData[fullPath.includes("sign-in") ? "sign-in" : fullPath.includes("sign-up") ? "sign-up" : "default"];
   
});
</script>

<template>
  <HeaderWebsite class="md:hidden" />
  <div class="grid grid-cols-1 md:grid-cols-2 h-screen">
    <Head>
      <Title>{{ $t(page.title) }}</Title>
    </Head>
    <div class="relative hidden md:block">
      <LogoActivist
      class="absolute inset-0 flex items-center justify-center mb-24 md:px-16 lg:px-32 xl:px-48"
      />
    </div>
    <div class="h-full text-light-text dark:text-dark-text bg-light-distinct dark:bg-dark-distinct">
      <div class="hiddem space-x-6 justify-end py-4 px-8 md:flex">
        <SelectorLanguage />
        <BtnLabeled
          class="flex items-center max-h-[40px]"
          :label="page.label"
          :linkTo="page.link"
          :cta="true"
          fontSize="lg"
          ariaLabel="SignIn"
        />
      </div>
      <div class="flex-1 w-full pt-24 md:pt-36 pb-4 md:pb-12 space-y-4">
        <div class="flex items-center justify-center p-4">
          <h1
            class="text-center xl:text-[64px] responsive-h1 font-bold font-display"
          >
            {{ $t(page.message) }}
          </h1>
          <!-- <Icon
            class="text-light-link-text dark:text-dark-link-text ml-6"
            :name="page.icon"
            size="3em"
          /> -->
        </div>
      </div>
      <slot />
    </div>
  </div>
</template>
