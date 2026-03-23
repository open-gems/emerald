<template>
  <PageSplit initialWidth="55%">
    <template #left>
      <MarkdownEditor />
    </template>
    <template #right>
      <div class="button-grid">
        <UButton
          v-for="(btn, index) in buttons"
          :key="index"
          :icon="btn.icon"
          size="lg"
          :color="btn.color"
          variant="outline"
          >{{ btn.label }}</UButton
        >
      </div>
      <USeparator />
      <div>
        exam
      </div>
    </template>
  </PageSplit>
</template>

<script setup>
import { ref } from "vue";

const buttons = ref([
  {
    label: "Quiz Question",
    color: "success",
    icon: "i-lucide-book-open-check",
  },
]);
</script>

<style lang="css" scoped>
.button-grid {
  padding: 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.grid-button {
  flex: 1 1 auto;
}
</style>
