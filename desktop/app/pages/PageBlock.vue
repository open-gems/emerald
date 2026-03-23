<template>
  <PageSplit initialWidth="55%">
    <template #left>
      <MarkdownEditor />
    </template>
    <template #right>
      <UButton
        icon="i-lucide-rocket"
        size="xl"
        color="primary"
        variant="outline"
        >Question</UButton
      >
    </template>
  </PageSplit>
</template>

<script setup></script>

<style lang="css" scoped></style>
