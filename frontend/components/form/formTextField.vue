<script setup lang="ts">
import useUniqueID from "~/composables/useUniqueID";
import useFormInput from "~/composables/useFormSetup";

const props = defineProps({
  placeholder: {
    type: String,
    default: "",
  },
  modelValue: {
    type: String,
    default: "",
  },
  inputType: {
    type: String,
    default: "text",
  },
  isIconVisible: {
    type: Boolean,
    default: false,
  },
  isInfoIconVisible: {
    type: Boolean,
    default: false,
  },
});
const emit = defineEmits(["update:modelValue"]);

const route = useRoute();

const { updateValue } = useFormInput({ value: props?.modelValue }, emit, false);

const uuid = useUniqueID().getID();

const refInputType = ref(props?.inputType)

const changeInputType = () => {
  refInputType.value = refInputType.value === "password" ? "text" : "password"
}

</script>

<template>
  <div
    class="flex items-center pl-[12px] pr-[10px] py-2 max-h-[40px] space-x-2 text-left border rounded select-none border-light-interactive dark:border-dark-interactive text-light-special-text dark:text-dark-special-text"
  >
    <input
      class="w-full h-5 bg-transparent outline-none placeholder:text-light-special-text dark:placeholder:text-dark-special-text"
      @input="updateValue"
      :id="uuid"
      :value="modelValue"
      :placeholder="placeholder"
      :type="refInputType"
      :isIconVisible="isIconVisible"
    />
    <span v-if="isInfoIconVisible" class="cursor-pointer"
    >
      <Icon name="mdi:alert-circle-outline" size="28px" />
    </span>
    <span v-if="isIconVisible" @click="changeInputType" class="cursor-pointer">
      <Icon name="mdi:eye" size="28px" />
    </span>
  </div>
</template>

<style scoped></style>
