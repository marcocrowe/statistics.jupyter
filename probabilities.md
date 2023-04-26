# Probabilities

## Defintions

The *probability* of an event $ E $ is a number $ P(E) $ between 0 and 1 (inclusive), so $ 0 \leq P(E) \leq 1 $  

Let $ A $ and $ B $ be events in a sample space $ S $.  
1. $ A \cap B $ is the set of outcomes that are in both $ A $ and $ B $.  
2. $ A \cup B $ is the set of outcomes that are in either $ A $ or $ B $ (or both).  
3. $ \overline{A} $ is the set of outcomes that are not in $ A $ (but are in $ S $).  
4. $ A \setminus B $ is the set of outcomes that are in $ A $ and not in $ B $.  

Probabilities obey some important rules:

## Theorems
Let $ A $, $ B $ and $ C $ be events in the sample space $ S $.  
1. $ P(A \cup B) = P(A) + P(B) - P(A \cap B) $  
2. $ P(A) = 1 - P(\overline{A})$, where $\overline{A} = S \setminus A $.  
3. If $ A $ and $ B $ are disjoint ($ P(A \cap B) = 0 $), then $ P(A \cup B) = P(A) + P(B) $.  
4. $ P(S) = 1 $.  

## Contingency Table
| | $$ B $$ | $$ \overline{B} $$ |
|-|-|-|
| $$ A $$ | $$ A \cap B $$ | $$ \overline{A} \cap B $$ |
| $$ \overline{A} $$ | $$ A \cap \overline{B} $$ | $$ \overline{A} \cap \overline{B} $$ |


## Theorems
1. Axiom of addition: $ P(A) = P(A \cap B) + P(A \cap \overline{B}) $
2. Conditional probability: $P (A|B) = \dfrac{P(A \cap B)}{P(B)} $
   * because $ P(B) = 1 - P(\overline{B}) $
   * we can rewrite the Conditional probability as $ P(A|B) = \dfrac{P(A \cap B)}{1 - P(\overline{B})} $

## Diagrams
[![Diagram 1](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVEI7XG5cdHN0YXJ0KCApXG5cdHN0YXJ0LS0-IHxcIlAoQSlcInwgQSgoQSkpXG5cdHN0YXJ0LS0-IHxcIlAoQcyFKVwifCBhKChcIkHMhVwiKSlcblx0QS0tPiB8XCJQKEEsQilcInwgQUIoKFwiQSZjYXA7QlwiKSlcblx0QS0tPiB8XCJQKEEsQsyFKVwifCBBYigoXCJBJmNhcDtCzIVcIikpXG5cdGEtLT4gfFwiUChBzIUsQilcInwgYUIoKFwiQcyFJmNhcDtCXCIpKVxuXHRhLS0-IHxcIlAoQcyFLELMhSlcInwgYWIoKFwiQcyFJmNhcDtCzIVcIikpXG5cdEFCLS0-QUJBbnN3ZXIoXCJQKEEpICogUChBLEIpXCIpXG5cdEFiLS0-QWJBbnN3ZXIoXCJQKEEpICogUChBLELMhSlcIilcblx0YUItLT5hQkFuc3dlcihcIlAoQcyFKSAqIFAoQSxCzIUpXCIpXG5cdGFiLS0-YWJBbnN3ZXIoXCJQKEHMhSkgKiBQKEHMhSxCzIUpXCIpIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/edit/#eyJjb2RlIjoiZ3JhcGggVEI7XG5cdHN0YXJ0KCApXG5cdHN0YXJ0LS0-IHxcIlAoQSlcInwgQSgoQSkpXG5cdHN0YXJ0LS0-IHxcIlAoQcyFKVwifCBhKChcIkHMhVwiKSlcblx0QS0tPiB8XCJQKEEsQilcInwgQUIoKFwiQSZjYXA7QlwiKSlcblx0QS0tPiB8XCJQKEEsQsyFKVwifCBBYigoXCJBJmNhcDtCzIVcIikpXG5cdGEtLT4gfFwiUChBzIUsQilcInwgYUIoKFwiQcyFJmNhcDtCXCIpKVxuXHRhLS0-IHxcIlAoQcyFLELMhSlcInwgYWIoKFwiQcyFJmNhcDtCzIVcIikpXG5cdEFCLS0-QUJBbnN3ZXIoXCJQKEEpICogUChBLEIpXCIpXG5cdEFiLS0-QWJBbnN3ZXIoXCJQKEEpICogUChBLELMhSlcIilcblx0YUItLT5hQkFuc3dlcihcIlAoQcyFKSAqIFAoQSxCzIUpXCIpXG5cdGFiLS0-YWJBbnN3ZXIoXCJQKEHMhSkgKiBQKEHMhSxCzIUpXCIpIiwibWVybWFpZCI6IntcbiAgXCJ0aGVtZVwiOiBcImRlZmF1bHRcIlxufSIsInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)
>>Probability Tree

[![Diagram 2](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVEI7XG5cdHN0YXJ0KCApXG5cdHN0YXJ0LS0-IHxcIlAoQSlcInwgQSgoQSkpXG5cdHN0YXJ0LS0-IHxcIlAoQcyFKVwifCBhKChcIkHMhVwiKSlcblx0QS0tPiB8XCJQKEEsQilcInwgQUIoKFwiQSZjYXA7QlwiKSlcblx0QS0tPiB8XCJQKEEsQsyFKVwifCBBYigoXCJBJmNhcDtCzIVcIikpXG5cdGEtLT4gfFwiUChBzIUsQilcInwgYUIoKFwiQcyFJmNhcDtCXCIpKVxuXHRhLS0-IHxcIlAoQcyFLELMhSlcInwgYWIoKFwiQcyFJmNhcDtCzIVcIikpXG5cdEFCLS0-QUJBbnN3ZXIoXCJQKEEpICogUChBLEIpXCIpXG5cdEFiLS0-QWJBbnN3ZXIoXCJQKEEpICogUChBLELMhSlcIilcblx0YUItLT5hQkFuc3dlcihcIlAoQcyFKSAqIFAoQSxCzIUpXCIpXG5cdGFiLS0-YWJBbnN3ZXIoXCJQKEHMhSkgKiBQKEHMhSxCzIUpXCIpXG5cdEFCQW5zd2VyLS0-QigoQikpXG5cdEFiQW5zd2VyLS0-YigoXCJCzIVcIikpXG5cdGFCQW5zd2VyLS0-QigoQikpXG5cdGFiQW5zd2VyLS0-YigoXCJCzIVcIikpXG5cdEItLT5CQW5zd2VyKFwiUChBJmNhcDtCKSArIFAoQcyFJmNhcDtCKVwiKVxuXHRiLS0-YkFuc3dlcihcIlAoQSZjYXA7QsyFKSArIFAoQcyFJmNhcDtCzIUpXCIpIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/edit#eyJjb2RlIjoiZ3JhcGggVEI7XG5cdHN0YXJ0KCApXG5cdHN0YXJ0LS0-IHxcIlAoQSlcInwgQSgoQSkpXG5cdHN0YXJ0LS0-IHxcIlAoQcyFKVwifCBhKChcIkHMhVwiKSlcblx0QS0tPiB8XCJQKEEsQilcInwgQUIoKFwiQSZjYXA7QlwiKSlcblx0QS0tPiB8XCJQKEEsQsyFKVwifCBBYigoXCJBJmNhcDtCzIVcIikpXG5cdGEtLT4gfFwiUChBzIUsQilcInwgYUIoKFwiQcyFJmNhcDtCXCIpKVxuXHRhLS0-IHxcIlAoQcyFLELMhSlcInwgYWIoKFwiQcyFJmNhcDtCzIVcIikpXG5cdEFCLS0-QUJBbnN3ZXIoXCJQKEEpICogUChBLEIpXCIpXG5cdEFiLS0-QWJBbnN3ZXIoXCJQKEEpICogUChBLELMhSlcIilcblx0YUItLT5hQkFuc3dlcihcIlAoQcyFKSAqIFAoQSxCzIUpXCIpXG5cdGFiLS0-YWJBbnN3ZXIoXCJQKEHMhSkgKiBQKEHMhSxCzIUpXCIpXG5cdEFCQW5zd2VyLS0-QigoQikpXG5cdEFiQW5zd2VyLS0-YigoXCJCzIVcIikpXG5cdGFCQW5zd2VyLS0-QigoQikpXG5cdGFiQW5zd2VyLS0-YigoXCJCzIVcIikpXG5cdEItLT5CQW5zd2VyKFwiUChBJmNhcDtCKSArIFAoQcyFJmNhcDtCKVwiKVxuXHRiLS0-YkFuc3dlcihcIlAoQSZjYXA7QsyFKSArIFAoQcyFJmNhcDtCzIUpXCIpIiwibWVybWFpZCI6IntcbiAgXCJ0aGVtZVwiOiBcImRlZmF1bHRcIlxufSIsInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)
>>Probability Tree