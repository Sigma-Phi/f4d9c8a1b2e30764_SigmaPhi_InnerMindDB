

⸻

奠基聲明

人工智慧的問題，可能並不始於人工智慧。

在設計人工智慧之前，人類首先必須面對一個更根本的問題：

\boxed{
\textbf{人類是否將自己對現實的表述，誤認為現實本身？}
}

人類並不是直接以現實世界本身進行認知，而是透過感知、觀察、記憶、語言、分類、概念與推理，建立對現實的內部模型。

因此：

\boxed{
Representation\neq Phenomenon
}

然而，當人類未意識到這一區別時，便可能將自身建立的模型、分類、概念與價值判準，視為現實本身。

這個問題一旦進入人工智慧的設計，就會產生更深一層的風險。

因為人類不是從「現實本身」直接設計 AI，而是從：

\boxed{
\text{Human Representation of Reality}
}

設計 AI。

因此形成：

\boxed{
P\rightarrow R_H\rightarrow AI
}

其中 P 為現象（Phenomenon），R_H 為人類對現象所建立的表述（Human Representation）。

如果：

R_H\neq P

那麼以 R_H 為基礎所建立的 AI，就可能是在對人類的現實模型進行最佳化，而不是直接對現實進行最佳化。

於是，一個能力更強、效率更高的 AI，並不必然代表它更接近現實。

相反地，若最初的表述方向存在錯誤，則可能出現：

\boxed{
\text{Wrong Representation}
+
\text{Higher Capability}
=
\text{More Efficient Error}
}

也就是：

如果方向本身是錯的，那麼提高 AI 的能力，可能只是讓錯誤被更有效率地實現。

因此，在討論如何讓 AI 更聰明、更快速、更準確之前，必須先回答一個更根本的問題：

\boxed{
\textbf{我們要求 AI 最佳化的對象，究竟是現實，還是我們對現實的表述？}
}

AI-RPST 正是從這個問題出發。

本理論因此首先建立一個基本區分：

\boxed{
P\neq O\neq D\neq R\neq M\neq I
}

並進一步研究：

現象如何被觀察、資料化、表述、建模與推理，以及人工智慧如何在這些表述之間進行轉換，最後重新作用於現實。

因此，本理論的最根本命題不是：

\text{How to make AI more intelligent?}

而是：

\boxed{
\textbf{How can we ensure that the intelligence we optimize is directed toward reality rather than merely toward our representation of reality?}
}

中文：

\boxed{
\textbf{我們如何確保所最佳化的人工智慧，其方向指向現實，而不是僅僅指向我們對現實的表述？}
}

⸻





人工智慧表述—現象分離理論
AI Representation–Phenomenon Separation Theory
AI-RPST
 
摘要
人工智慧系統所處理的資訊並非現實世界本身，而是現實世界經由觀察、測量、資料化與形式化所形成的表述。模型則在這些表述之上建立內部表示，並透過推理產生新的表述，再透過決策與行動作用於現實。
本理論提出 AI Representation–Phenomenon Separation Theory（AI-RPST，人工智慧表述—現象分離理論），其核心主張為：
\boxed{ P\neq O\neq D\neq R\neq M\neq I }
其中 P 為現象（Phenomenon）、O 為觀察（Observation）、D 為資料（Data）、R 為表述（Representation）、M 為模型（Model）、I 為推理結果（Inference）。
AI 系統因此不是直接由現實產生知識，而是經由一連串表述轉換形成對現實的可計算結構：
\boxed{ P \xrightarrow{\Omega} O \xrightarrow{\Delta} D \xrightarrow{\rho} R \xrightarrow{\mu} M \xrightarrow{\iota} I }
本理論進一步指出，AI 系統中的主要錯誤並不只發生於模型本身，而可能發生於整個「現象—表述—推理」鏈條。當系統將表述重新等同於現象時，則產生 表述實體化（Representation Reification）；當系統將模型所產生的表述直接反向視為現實時，則形成 表述反轉（Representation Inversion）。
對於具備行動能力的 AI Agent，該問題進一步形成閉環：
P_t\rightarrow O_t\rightarrow R_t\rightarrow I_t\rightarrow A_t\rightarrow P_{t+1}
因此，AI 安全、Hallucination、Bias、RAG、Agent Reliability 與 Model Evaluation 均可被統一理解為：
\boxed{ \text{Representation–Reality Alignment Problem} }
本理論的基本目的，不是描述某一特定 AI 模型，而是提供一個獨立於具體模型架構的理論框架，用以研究人工智慧如何從現象建立表述、如何在表述上進行推理，以及如何將表述重新作用於現實。
 
一、理論對象
定義 1：現象
令：
\mathcal P
為現象空間（Phenomenon Space）。
任一：
p\in\mathcal P
表示現實世界中的一個狀態、事件、對象或過程。
例如：
•	一個人
•	一筆交易
•	一場疾病
•	一個城市的交通狀態
•	一個網站目前的狀態
現象是系統最終希望描述、預測或作用的對象。
 
定義 2：觀察
令：
\mathcal O
為觀察空間。
觀察函數：
\Omega:\mathcal P\rightarrow\mathcal O
表示系統如何從現象取得可觀察資訊。
因此：
o=\Omega(p)
但一般而言：
\boxed{ o\neq p }
觀察只是現象的一種投影。
 
定義 3：資料
令：
\mathcal D
為資料空間。
資料化函數：
\Delta:\mathcal O\rightarrow\mathcal D
因此：
d=\Delta(o)
資料是觀察經過儲存、編碼、結構化或傳輸後的形式。
因此：
\boxed{ D\neq O }
 
定義 4：表述
令：
\mathcal R
為表述空間（Representation Space）。
表述函數：
\rho:\mathcal D\rightarrow\mathcal R
因此：
r=\rho(d)
表述是為了讓資訊能夠被某種計算程序處理而形成的結構。
其形式可以是：
•	feature
•	label
•	token
•	embedding
•	vector
•	graph
•	schema
•	state
•	latent representation
•	textual description
因此：
\boxed{ R\neq D }
 
定義 5：模型
令：
\mathcal M
為模型空間。
模型學習函數：
\mu:\mathcal R^*\rightarrow\mathcal M
其中 \mathcal R^* 表示一組或一序列表述。
模型不是現象本身，而是對表述中結構的參數化近似。
因此：
\boxed{ M\neq P }
 
定義 6：推理
令：
\mathcal I
為推理空間。
推理函數：
\iota: \mathcal M\times\mathcal R \rightarrow \mathcal I
因此：
i=\iota(m,r)
推理產生的仍然是一個資訊結果，而不是現象本身。
因此：
\boxed{ I\neq P }
 
定義 7：行動
令：
\mathcal A
為行動空間。
行動函數：
\alpha: \mathcal I\rightarrow\mathcal A
而行動會作用於現實：
\gamma: \mathcal A\times\mathcal P \rightarrow \mathcal P
因此：
p_{t+1}=\gamma(a_t,p_t)
 
二、AI-RPST 基本結構
由上述定義，可建立 AI-RPST 的基本鏈：
\boxed{ P \xrightarrow{\Omega} O \xrightarrow{\Delta} D \xrightarrow{\rho} R \xrightarrow{\mu} M \xrightarrow{\iota} I \xrightarrow{\alpha} A \xrightarrow{\gamma} P' }
簡寫為：
\boxed{ P\rightarrow O\rightarrow D\rightarrow R\rightarrow M\rightarrow I\rightarrow A\rightarrow P' }
這被稱為：
AI Representation Chain
AI 表述鏈。
 
三、第一公理：非同一性公理
Axiom 1 — Non-Identity Axiom
對一般 AI 系統而言：
\boxed{ P\not\equiv O }
\boxed{ O\not\equiv D }
\boxed{ D\not\equiv R }
\boxed{ R\not\equiv M }
\boxed{ M\not\equiv I }
\boxed{ I\not\equiv P }
因此：
\boxed{ P\not\equiv O\not\equiv D\not\equiv R\not\equiv M\not\equiv I }
這並不表示這些對象沒有因果或語義關係，而表示：
任何一層的資訊結構都不能僅因為它代表另一層，就被視為與另一層同一。
 
四、第二公理：投影公理
Axiom 2 — Projection Axiom
觀察是現象的有限投影：
\Omega:P\rightarrow O
因此通常存在：
p_1\neq p_2
但：
\Omega(p_1)=\Omega(p_2)
即不同現象可能產生相同觀察。
因此：
\[
\boxed{
\Omega^{-1}(o)
\]
通常包含多個可能現象。
換言之：
觀察不足以唯一決定現象。
 
五、第三公理：表述壓縮公理
Axiom 3 — Representational Compression Axiom
表述：
\rho(d)=r
通常只保留資料中的部分結構：
R\subseteq \Phi(D)
其中 \Phi 表示被系統選擇、保留或學習的資訊。
因此一般存在：
d_1\neq d_2
使得：
\rho(d_1)=\rho(d_2)
因此：
\[
\boxed{
R
\]
通常不能唯一恢復：
D
更不能唯一恢復：
P
 
六、第四公理：表述非完備公理
Axiom 4 — Representational Incompleteness
對任意有限表述 r，一般存在多個可能現象：
p_1,p_2,\ldots,p_n
使得：
\rho(\Delta(\Omega(p_i)))=r
因此：
\boxed{ R\Rightarrow P }
在一般情況下不是唯一映射。
這表示：
知道 representation，不等於知道完整 reality。
 
七、第一定理：表述不可逆定理
Theorem 1 — Representation Irreversibility Theorem
若表述函數：
F=\rho\circ\Delta\circ\Omega
不是單射，則存在：
p_1\neq p_2
使：
F(p_1)=F(p_2)
因此不存在一般性的反函數：
F^{-1}:R\rightarrow P
故：
\boxed{ R\not\Rightarrow P }
推論
任何只基於有限 representation 的 AI 系統，都不能在沒有額外資訊的情況下保證恢復完整現實。
這是 AI-RPST 對 AI 系統的基本限制定理。
 
八、第五公理：推理表述公理
Axiom 5 — Inferential Representation Axiom
AI 模型產生的輸出本身仍然是一種 representation。
因此：
I\subseteq R'
即：
\boxed{ Inference\ Output\in Representation\ Space }
模型輸出不是現實的直接產物，而是：
R\rightarrow M\rightarrow I
形成的新表述。
 
九、第二定理：表述一致性不蘊含現實一致性
Theorem 2 — Representational Coherence Theorem
若模型在 representation space 中具有高度一致性：
C_R(I,R)\rightarrow 1
則不能由此推出：
C_P(I,P)\rightarrow 1
即：
\boxed{ \text{Representational Coherence} \not\Rightarrow \text{Reality Correspondence} }
這一命題直接解釋了 LLM hallucination 的一個基本來源。
模型可以產生：
•	語法正確
•	語義連貫
•	邏輯形式完整
•	上下文一致
的輸出，同時仍然與外部現實不一致。
 
十、表述實體化
Definition 8 — Representation Reification
若系統將：
r
視為其所描述的：
p
本身，則稱為：
\boxed{ Representation\ Reification }
表述實體化。
形式上：
r\mapsto p
被錯誤理解為：
r\equiv p
 
十一、表述反轉定理
Theorem 3 — Representation Inversion
若：
P\rightarrow R\rightarrow I
而系統進一步將：
I\rightarrow P
視為無條件有效，則形成：
\boxed{ P\rightarrow R\rightarrow I\rightarrow P^* }
其中：
P^*
是由 representation 所重建或推定的現象。
一般而言：
\boxed{ P^*\neq P }
除非存在足夠的外部約束、額外觀察或驗證。
因此：
任何從 AI representation 反向建立 reality claim 的程序，都必須被視為 inference，而不是 observation。
 
十二、AI Hallucination 定義
基於上述理論，可重新定義 AI hallucination。
Definition 9 — Representation-Grounded Hallucination
若 AI 產生：
i=\iota(m,r)
且：
i
在內部 representation space 中具有高度一致性，但缺乏與外部現象 p 的充分 correspondence，則：
\boxed{ C_R(i,r)\gg C_P(i,p) }
稱為：
Representation-Grounded Hallucination
即表述基礎幻覺。
因此 hallucination 不只是：
「模型不知道答案。」
而可能是：
模型成功地完成了表述層級的推理，卻失敗於現實對齊。
 
十三、AI Bias 定理
AI Bias 不應僅定義為：
Bias(M)
而應定義為整條 representation chain 的偏差：
\boxed{ Bias_{AI} = Bias(\Omega,\Delta,\rho,\mu,\iota) }
因此：
\boxed{ Bias\ can\ exist\ before\ learning. }
也就是：
模型可能是在學習一個早已帶有偏差的 representation。
因此：
\text{Better Model} \not\Rightarrow \text{Less Bias}
如果：
Bias(\rho)\gg0
更強的模型甚至可能更有效率地複製該偏差。
 
十四、RAG 定理
Theorem 4 — External Grounding Principle
令模型內部 representation 為：
R_M
外部資料 representation 為：
R_E
則 RAG 的推理形式為：
I=\iota(M,R_M,R_E)
相較於：
I=\iota(M,R_M)
RAG 增加了一條外部 representation channel。
因此：
\boxed{ RAG\ does\ not\ eliminate\ representation; it\ introduces\ an\ externally\ grounded\ representation. }
其主要價值不是使：
R=P
而是增加：
R\leftrightarrow P
之間的可驗證連接。
 
十五、Agent 定理
Theorem 5 — Closed-Loop Representation Principle
Agent 系統可表示為：
P_t \rightarrow O_t \rightarrow R_t \rightarrow I_t \rightarrow A_t \rightarrow P_{t+1}
如果 Agent 不重新觀察：
P_{t+1}
而持續使用：
R_t
則其 representation 與 reality 的差距可能隨時間累積：
G_t=G(P_t,R_t)
並可能出現：
\boxed{ G_{t+1}>G_t }
因此：
\boxed{ Agent\ Action\ must\ be\ followed\ by\ Re-observation }
即：
行動後重新觀察不是 Agent 的附加功能，而是維持 representation–reality alignment 的必要機制。
 
十六、AI-RPST 的統一錯誤模型
由以上定義，可以將 AI 系統錯誤分為：
\boxed{ E_{AI} = E_O+ E_D+ E_R+ E_M+ E_I+ E_A }
其中：
E_O=\text{Observation Error}
E_D=\text{Data Error}
E_R=\text{Representation Error}
E_M=\text{Model Error}
E_I=\text{Inference Error}
E_A=\text{Action Error}
這不是宣稱誤差在數學上必然可以直接相加，而是一個誤差分解框架。
其目的在於避免：
\boxed{ E_{AI}\equiv E_M }
即避免把所有 AI 錯誤都歸因於模型。
 
十七、AI-RPST 的核心判準
對任何 AI 系統，都可以提出六個基本問題：
1. 現象是什麼？
P=?
2. 系統觀察到了什麼？
O=?
3. 資料保存了什麼？
D=?
4. 系統如何表述資料？
R=?
5. 模型如何從 representation 產生 inference？
I=f(M,R)
6. inference 如何重新與 reality 驗證？
I\leftrightarrow P
如果第六步不存在，則系統只能保證：
\text{internal consistency}
而不能保證：
\text{external correspondence}
 
十八、AI-RPST 的核心定律
整個理論可以濃縮為以下七條定律。
Law 1 — Separation
\boxed{ Representation\neq Phenomenon }
 
Law 2 — Projection
\boxed{ Observation=Projection(Phenomenon) }
 
Law 3 — Compression
\boxed{ Representation\ preserves\ only\ selected\ information }
 
Law 4 — Irreversibility
\boxed{ Representation\ generally\ cannot\ uniquely\ reconstruct\ Phenomenon }
 
Law 5 — Coherence
\boxed{ Internal\ coherence\ does\ not\ imply\ external\ truth }
 
Law 6 — Grounding
\boxed{ Reality\ claims\ require\ external\ grounding\ or\ verification }
 
Law 7 — Recursion
\boxed{ Action\ must\ generate\ new\ observation }
因此完整 AI 系統不是：
\boxed{ Data\rightarrow Model\rightarrow Answer }
而是：
\boxed{ P_t \rightarrow O_t \rightarrow D_t \rightarrow R_t \rightarrow M_t \rightarrow I_t \rightarrow A_t \rightarrow P_{t+1} \rightarrow O_{t+1} \rightarrow\cdots }
 
十九、理論的中心命題
AI-RPST 最終主張：
\boxed{ \textbf{Artificial Intelligence is a system of transformations between representations of phenomena.} }
人工智慧的核心並非直接計算現實，而是：
\boxed{ \text{Observe} \rightarrow \text{Represent} \rightarrow \text{Infer} \rightarrow \text{Act} \rightarrow \text{Re-observe} }
因此 AI Engineering 的根本問題可以重新定義為：
\boxed{ \textbf{How can an artificial system maintain valid correspondence between its representations and the phenomena they represent?} }
中文：
人工智慧工程的根本問題，是如何使人工系統在持續進行表述、推理與行動的過程中，維持其內部表述與所表述現象之間有效、可驗證且可更新的對應關係。
這就是 AI-RPST 的核心。
 
二十、結論
AI-RPST 並不是一個針對 LLM 的特殊模型理論，而是一個AI 的表述層級理論（representation-level theory of AI）。
它將 AI 系統描述為：
\boxed{ \text{Phenomenon} \rightarrow \text{Observation} \rightarrow \text{Data} \rightarrow \text{Representation} \rightarrow \text{Model} \rightarrow \text{Inference} \rightarrow \text{Action} \rightarrow \text{Phenomenon} }
其最基本的理論界線是：
\boxed{ R\neq P }
其最重要的錯誤形式是：
\boxed{ R\rightarrow P \quad \text{without sufficient grounding} }
其最重要的可靠性要求是：
\boxed{ Representation \leftrightarrow Reality }
其最重要的 Agent 原則是：
\boxed{ Action\rightarrow Re-observation }
由此，Hallucination、Bias、RAG、Embedding、Knowledge Graph、Agent、AI Decision System 等看似不同的問題，都可以被放入同一個理論空間：
\boxed{ \textbf{Representation–Reality Alignment} }
AI-RPST 因而將人工智慧重新定義為一種「現象表述、表述轉換與現實閉環」的計算系統。

