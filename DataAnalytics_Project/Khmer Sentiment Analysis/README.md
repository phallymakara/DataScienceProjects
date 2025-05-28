# 🇰🇭 Khmer Sentiment Analysis with XLM-RoBERTa

This project focuses on building a **Khmer sentiment classifier** using the **XLM-RoBERTa transformer architecture**, with a crucial preprocessing step: **Khmer word segmentation**. Due to the nature of the Khmer language (which lacks clear word boundaries), segmentation significantly boosts tokenization quality and downstream performance.

## 📌 Objective

To classify Khmer text into **positive** or **negative** sentiment by fine-tuning a multilingual transformer model.

## 🧠 Model Architecture

- **Model**: `xlm-roberta-base`
- **Approach**: Fine-tuning for binary classification
- **Key Step**: Khmer word segmentation before applying tokenizer
- **Framework**: Hugging Face Transformers + PyTorch

## 🛠️ Tools & Libraries

- Python
- Hugging Face Transformers, Datasets
- PyTorch
- Khmer Word Segmentation Library (e.g., `khmernltk`, `pykhmer` or custom)
- Google Colab (for experimentation)

## 📁 Workflow

1. **Data Preparation**
   - Load labeled Khmer sentiment dataset
   - Apply **Khmer word segmentation**
   - Tokenize using `XLMRobertaTokenizer`
2. **Model Setup**
   - Load `xlm-roberta-base` for sequence classification
3. **Training**
   - Fine-tune on segmented and tokenized data
4. **Evaluation**
   - Metrics: Accuracy, Precision, Recall, F1-score
5. **Inference**
   - Predict sentiment on new Khmer text

## 📊 Dataset

- Binary labeled dataset: `0` = negative, `1` = positive
- Custom Khmer text data
- Segmented prior to training

## ✅ Performance

| Metric     | Value    |
|------------|----------|
| Accuracy   | ~72%     |
| F1-Score   | ~71%     |

> Khmer segmentation significantly improves the quality of tokenization and downstream classification results.

## ⚠️ Challenges

- Scarcity of large-scale labeled Khmer data
- Reliable Khmer word segmentation tools
- Pretrained models may underperform on low-resource languages

## 🔭 Future Directions

- Train on larger, domain-specific Khmer datasets
- Experiment with Khmer-specific pretraining or adapters
- Serve the model as an inference API

## 💡 Use Cases

- Khmer social media monitoring
- Customer feedback analysis
- Educational sentiment tools
