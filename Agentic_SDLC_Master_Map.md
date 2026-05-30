# Bản đồ Quy trình & Luồng Vận hành Agentic SDLC (Master Visual Map)

Tài liệu này tổng hợp và trực quan hóa toàn bộ vòng đời phát triển phần mềm bằng AI Agent (Agentic SDLC). Các sơ đồ dưới đây giúp bạn dễ dàng hình dung từ khâu thiết lập ý định, lập kế hoạch, viết code, kiểm thử, duyệt tích hợp (Merge Gate) cho đến giám sát vận hành 24/7 và cơ chế tự động học hỏi, cải tiến liên tục.

---

## 1. Bản đồ Toàn cảnh Quy trình Agentic SDLC (Master Landscape Map)
Sơ đồ dưới đây bao quát 8 pha trong vòng đời phát triển Agentic (ADLC), làm rõ mối quan hệ giữa **các hoạt động**, **các bên chịu trách nhiệm (Vai trò)**, **các Artifact sinh ra** và **cách con người kiểm soát (HITL)**.

```mermaid
flowchart TB
    subgraph Phase1["Pha 1: Đặc tả ý định (Intent & Constraints)"]
        direction TB
        P1_In["Yêu cầu nghiệp vụ (Business Requirement)"] --> P1_Act["Đặc tả mục tiêu, tiêu chí hoàn thành (DoD), ràng buộc & ngân sách"]
        P1_Act --> P1_Art["Artifacts:<br/>- Feature Spec<br/>- UI/Component Contracts<br/>- Module Contracts"]
    end

    subgraph Phase2["Pha 2: Lập kế hoạch (Planning & Phân rã)"]
        direction TB
        P2_In["Artifacts của Pha 1"] --> P2_Act["Phân tách nhiệm vụ thành các task nhỏ, lập sơ đồ sở hữu (Ownership Map) & xác định rủi ro"]
        P2_Act --> P2_Art["Artifacts:<br/>- Agent Task Brief<br/>- ADR (Architecture Decision Record)"]
    end

    subgraph Phase3["Pha 3: Thực thi (Build / Action)"]
        direction TB
        P3_In["Task Brief & Constraints"] --> P3_Act["Thực thi code/thao tác trong nhánh cô lập (Isolated Worktree/Branch)"]
        P3_Act --> P3_Art["Artifacts:<br/>- Mã nguồn (Source Code)<br/>- Tests mới"]
    end

    subgraph Phase4["Pha 4: Kiểm thử & Đánh giá (Validation & Evals)"]
        direction TB
        P4_In["Source Code & Tests"] --> P4_Act["Chạy CI tự động: Unit Evals, LLM-as-judge Regression, Visual Regression, Contract Tests"]
        P4_Act --> P4_Art["Artifacts:<br/>- Báo cáo kết quả Evals & Tests"]
    end

    subgraph Phase5["Pha 5: Review & Duyệt (Human Checkpoint - HITL)"]
        direction TB
        P5_In["Báo cáo Evals"] --> P5_Act["Con người duyệt tại checkpoint đối với các hành động rủi ro trung bình/cao"]
        P5_Act --> P5_Art["Artifacts:<br/>- Merge Gate Report"]
    end

    subgraph Phase6["Pha 6: Triển khai (Deploy / Ship)"]
        direction TB
        P6_In["Merge Gate Approved"] --> P6_Act["Tích hợp mã nguồn vào nhánh chính & deploy thông qua cổng chất lượng tự động"]
        P6_Act --> P6_Art["Artifacts:<br/>- Release Note<br/>- Production Deployment"]
    end

    subgraph Phase7["Pha 7: Vận hành & Quan sát (Operate 24/7)"]
        direction TB
        P7_In["Production Deployment"] --> P7_Act["Vận hành 24/7, giám sát traces OpenTelemetry, metrics chi phí & độ tin cậy"]
        P7_Act --> P7_Art["Artifacts:<br/>- Telemetry Traces<br/>- Dashboards & Alerts"]
    end

    subgraph Phase8["Pha 8: Học & Tự cải thiện (Learn & Self-Improvement)"]
        direction TB
        P8_In["Telemetry Traces & Logs"] --> P8_Act["Phân tích lỗi tự động, đề xuất nâng cấp Prompt/Skill, thử nghiệm sandbox"]
        P8_Act --> P8_Art["Artifacts:<br/>- Prompt/Skill cập nhật<br/>- Memory bổ sung"]
    end

    %% Kết nối giữa các Pha
    Phase1 --> Phase2
    Phase2 --> Phase3
    Phase3 --> Phase4
    Phase4 --> Phase5
    Phase5 -->|Duyệt| Phase6
    Phase5 -->|Từ chối / Yêu cầu sửa| Phase2
    Phase6 --> Phase7
    Phase7 --> Phase8
    Phase8 -.->|"Cập nhật ý định/ràng buộc (Vòng lặp học hỏi)"| Phase1
    Phase7 -.->|"Sự cố hoặc Drift"| Phase4

    %% Styling
    classDef human fill:#d1e7dd,stroke:#0f5132,stroke-width:2px;
    classDef agent fill:#cff4fc,stroke:#087990,stroke-width:2px;
    classDef gate fill:#fff3cd,stroke:#664d03,stroke-width:2px;
    classDef learn fill:#f8d7da,stroke:#842029,stroke-width:2px;

    class Phase1,Phase5 human;
    class Phase2,Phase3 agent;
    class Phase4,Phase6 gate;
    class Phase7,Phase8 learn;
```

---

## 2. Sơ đồ Trình tự Phát triển Tính năng (Feature Development Sequence Diagram)
Sơ đồ trình tự thời gian thể hiện sự phối hợp chặt chẽ giữa các vai trò Con người, AI Supervisor, AI Coding Agents, hệ thống kiểm thử CI/CD và giám sát vận hành:

```mermaid
sequenceDiagram
    autonumber
    actor PO as Product Owner
    actor Arch as Architect / Designer
    actor Dev as Developer / Lead
    participant Sup as Supervisor Agent
    participant Agent as Coding Agent
    participant CI as CI/CD & Evals
    participant Obs as Observe System

    Note over PO, Dev: Giai đoạn 1: Chuẩn bị & Đóng băng
    PO->>Arch: Gửi Feature Spec & Nghiệp vụ
    Arch->>Arch: Thiết lập Design Tokens & ADR
    Arch->>Dev: Đóng băng kiến trúc (Architecture Freeze)
    Dev->>Sup: Giao Task Brief, Contracts & Ràng buộc

    Note over Sup, Agent: Giai đoạn 2: Lập kế hoạch & Thực thi
    Sup->>Sup: Lập kế hoạch phân rã Task & Ownership Map
    Sup->>Agent: Tạo isolated branch & Giao Task
    loop Tự sửa lỗi (Self-Correction Loop)
        Agent->>Agent: Viết code trong Sandbox
        Agent->>Agent: Chạy test nội bộ & Tự sửa lỗi
    end
    Agent->>Sup: Hoàn thành nhiệm vụ & Đẩy mã nguồn

    Note over Sup, CI: Giai đoạn 3: Kiểm định tự động & Duyệt
    Sup->>CI: Kích hoạt Pipeline Evals
    activate CI
    CI->>CI: Chạy Unit Evals & Contract Tests
    CI->>CI: Chạy Visual Regression & LLM-as-judge
    CI-->>Sup: Báo cáo kết quả kiểm tra
    deactivate CI
    Sup->>Sup: Tạo Merge Gate Report
    Sup->>Dev: Gửi PR & Merge Gate Report (HITL Checkpoint)
    alt Đạt chất lượng & Duyệt
        Dev->>CI: Xác nhận Merge PR & Deploy
        CI->>Obs: Deploy lên Production thành công
    else Thất bại hoặc Cần điều chỉnh
        Dev->>Sup: Phản hồi lỗi & Từ chối merge
        Sup->>Agent: Yêu cầu sửa đổi kèm feedback
    end

    Note over Obs, Dev: Giai đoạn 4: Vận hành & Giám sát 24/7
    Obs->>Obs: Tracing OTel GenAI & Theo dõi chi phí
    alt Sự cố / Runaway Loop / Trôi chất lượng (Drift)
        Obs->>Obs: Kích hoạt Circuit Breaker / Fallback
        Obs-->>Dev: Alert cảnh báo lỗi để con người xử lý (HITL)
    end
```

---

## 3. Sơ đồ Trạng thái Nhiệm vụ của Agent (Agent Task Lifecycle State Diagram)
Theo dõi trạng thái của một nhiệm vụ dưới sự thực thi của AI Agent, bao gồm cả vòng lặp tự sửa lỗi (Self-Correction) và kiểm thử chất lượng:

```mermaid
stateDiagram-v2
    [*] --> Created : Giao Task Brief
    Created --> Planning : Xác thực ý định & ràng buộc
    Planning --> InSandbox : Đã chốt kế hoạch thực thi

    state InSandbox {
        [*] --> Executing : Đọc/Viết file & Gọi Tool
        Executing --> Compiling : Trình biên dịch/Linter
        Compiling --> Executing : Có lỗi syntax (Tự sửa)
        Compiling --> DoneCode : Compile thành công
    }

    InSandbox --> SelfTesting : Bắt đầu chạy test tự động
    
    state SelfTesting {
        [*] --> RunningTests : Chạy bộ Test đơn vị
        RunningTests --> FixingCode : Test thất bại
        FixingCode --> RunningTests : Cập nhật code & chạy lại
        RunningTests --> DoneTesting : 100% Test thành công
    }

    SelfTesting --> Evaluating : Chạy bộ Eval chất lượng nâng cao (Offline Evals)
    
    state Evaluating {
        [*] --> UnitEvals : Chạy Unit Evals
        UnitEvals --> LLM_Judge : Chạy LLM-as-judge
        LLM_Judge --> ContractTests : Chạy Contract Tests
        ContractTests --> PassedAll : Tất cả Evals đạt chỉ số baseline
    }

    Evaluating --> AwaitingReview : Đẩy PR & Gửi báo cáo Merge Gate
    Evaluating --> Planning : Thất bại Evals (Thiếu ngữ cảnh/Chệch mục tiêu)
    
    AwaitingReview --> Approved : Con người chấp thuận (HITL)
    AwaitingReview --> Planning : Con người từ chối (Góp ý/Thay đổi spec)
    
    Approved --> Merged : Thực hiện merge & đóng nhánh
    Merged --> [*]
```

---

## 4. Sơ đồ Kiến trúc Vận hành 24/7 & Xử lý lỗi (24/7 Operation & Error Recovery Architecture)
Mô tả cơ chế chạy liên tục của Agent trong môi trường Production cùng với các lớp phòng vệ (Guardrails) và khả năng tự đứng dậy (Error Recovery):

```mermaid
flowchart TB
    %% Inputs and entry
    Event["Sự kiện / API Request / Lịch biểu Cron"] --> GuardIn["Lớp Guardrail đầu vào (Input Guardrails)<br/>- Lọc prompt injection<br/>- Kiểm tra policy quyền hạn<br/>- Phân loại ý đồ"]

    %% Core routing
    GuardIn -->|Hợp lệ| AgentCore["Lõi Agent (Agent Core)<br/>- Lập kế hoạch (Reasoner)<br/>- Trí nhớ ngắn/dài hạn<br/>- Gọi Tools / APIs"]
    GuardIn -->|Vi phạm| Reject["Từ chối & Ghi log bảo mật"]

    %% Output verification
    AgentCore --> GuardOut["Lớp Guardrail đầu ra (Output Guardrails)<br/>- Kiểm duyệt nội dung<br/>- Chặn hành động rủi ro cao<br/>- Lọc dữ liệu nhạy cảm (PII)"]

    %% Execution and results
    GuardOut -->|Hợp lệ| Action["Hành động thực tế<br/>(Write database / Gọi API ngoài / Trả phản hồi)"]
    GuardOut -->|Vi phạm| SandboxFix["Chặn & Gửi lỗi ngược lại Agent để sửa đổi"]

    %% Observability Layer
    AgentCore -. Trace dữ liệu .-> OTel["Tracing (OpenTelemetry GenAI)<br/>- Theo dõi chuỗi quyết định (Trace)<br/>- Ghi nhận Tool call & Token cost"]
    OTel --> EvalOnline["Online Evaluation<br/>- Lấy mẫu đánh giá thực tế (Sampling)"]
    EvalOnline --> Alerts["Hệ thống cảnh báo (Alerting)<br/>- Vòng lặp runaway loop?<br/>- Chi phí vượt hạn mức?<br/>- Lỗi hệ thống?"]

    %% Error Recovery loop
    AgentCore -->|Gặp lỗi Tool/API/Logic| ErrRecover{"Bộ Xử lý lỗi (Error Recovery)"}
    ErrRecover -->|Lỗi nhẹ / có thể tự sửa| Retry["Retry với Exponential Backoff & Fallback Tool"]
    Retry --> AgentCore
    ErrRecover -->|Dependency hỏng liên tục| CircuitBreaker["Circuit Breaker<br/>- Tạm ngắt kết nối dịch vụ"]
    ErrRecover -->|Lỗi nặng / Runaway Loop| HITL["Escalate tới Con người (HITL)<br/>- Tạm dừng agent<br/>- Gửi thông báo khẩn cấp"]

    Alerts -->|Bất thường vượt ngưỡng| HITL

    %% Styling
    classDef core fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef security fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef obs fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef recovery fill:#fff3e0,stroke:#e65100,stroke-width:2px;

    class AgentCore core;
    class GuardIn,GuardOut,Reject security;
    class OTel,EvalOnline,Alerts obs;
    class ErrRecover,Retry,CircuitBreaker,HITL recovery;
```

---

## 5. Sơ đồ Vòng lặp Tự cải thiện liên tục (Continuous Self-Improvement Loop)
Mô phỏng cách hệ thống tự học từ các dữ liệu vận hành thực tế mà vẫn đảm bảo tính an toàn cao (không gây lỗi regression):

```mermaid
flowchart LR
    %% Main path
    Prod["Vận hành thực tế (Production)"] --> TraceLogs["Thu thập Traces & Logs (OTel)"]
    TraceLogs --> FailAnalysis["Phân tích lỗi tự động<br/>(Failure Analysis)"]
    FailAnalysis --> GenImprove["Đề xuất phương án cải tiến<br/>(Prompt / Skill / Memory / Tool mới)"]
    
    %% Sandbox verification
    GenImprove --> SandboxEval["Thử nghiệm trong Sandbox<br/>(Offline Eval Suite)"]
    SandboxEval --> RegressionCheck{"Đạt chỉ số & không Regression?"}
    
    %% Deployment Decisions
    RegressionCheck -->|Không đạt| Discard["Hủy bỏ & phân tích lại lỗi"]
    RegressionCheck -->|Đạt| Canary["Triển khai dần (Canary / A-B Testing)"]
    
    %% Return path
    Canary --> CompareProd["So sánh hiệu năng thực tế"]
    CompareProd -->|Tốt hơn| MergeMain["Tích hợp chính thức vào Production"]
    CompareProd -->|Tệ hơn| Rollback["Rollback về phiên bản cũ"]
    
    MergeMain --> Prod
    Discard -.-> FailAnalysis
    Rollback -.-> FailAnalysis

    %% Styling
    classDef sandbox fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef decision fill:#f8d7da,stroke:#842029,stroke-width:2px;
    classDef prod fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;

    class SandboxEval sandbox;
    class RegressionCheck,CompareProd decision;
    class Prod,Canary,MergeMain prod;
```

---

## 6. Bản đồ Cổng Kiểm soát Chất lượng Doanh nghiệp (Enterprise Quality Control Gates Map)
Trực quan hóa ma trận kiểm soát chất lượng (Quality Control Matrix), đảm bảo các đầu ra kỹ thuật luôn tuân thủ các chuẩn chung trước khi tích hợp vào nhánh chính:

```mermaid
flowchart TB
    %% Pillars
    subgraph UIUX["Cổng Chất lượng UI/UX"]
        direction TB
        Tokens["Design Tokens (Nguồn sự thật)"] --> TokenLint["Linter kiểm tra hard-code style"]
        TokenLint --> VisualReg["Chạy Visual Regression (So sánh Screenshot Diff)"]
        VisualReg --> A11y["Kiểm tra Responsive & Accessibility"]
        A11y --> DesignerReview["Designer Checkpoint (Con người duyệt)"]
    end

    subgraph Arch["Cổng Chất lượng Kiến trúc"]
        direction TB
        ADR["Duyệt ADR + Rollback Path"] --> ArchTests["Architecture Tests (Dependency Rules)"]
        ArchTests --> SecScans["Quét bảo mật (Security Scans & Threat Mitigation)"]
        SecScans --> ArchitectReview["Architect + Security Lead Review (HITL)"]
    end

    subgraph Domain["Cổng Chất lượng Module lớn"]
        direction TB
        Contracts["Xác lập Interface Contract & Domain Map"] --> ContractTests["Consumer-Driven Contract Tests"]
        ContractTests --> IntegTests["Integration Tests (Kiểm thử liên hợp)"]
        IntegTests --> E2E["E2E Nghiệp vụ (Kiểm thử luồng đầu-cuối)"]
        E2E --> DomainReview["Domain Owner Review & Approval"]
    end

    subgraph MultiAgent["Cổng Kiểm soát Multi-Agent"]
        direction TB
        TaskMap["Lập Task Ownership Map & Isolated Branches"] --> BranchCI["CI chạy độc lập trên từng Branch"]
        BranchCI --> BudgetGuard["Budget/Loop Guards & Trace Tracking"]
        BudgetGuard --> SupervisorReview["Supervisor / Tech Lead Review"]
    end

    %% Convergence
    DesignerReview --> MergeGate{"Hộp Tích hợp chính (Master Merge Gate)"}
    ArchitectReview --> MergeGate
    DomainReview --> MergeGate
    SupervisorReview --> MergeGate

    MergeGate -->|Tất cả thông qua| Ship["Merge & Release Code"]
    MergeGate -->|Có cổng thất bại| Block["Từ chối & Yêu cầu sửa đổi"]

    %% Styling
    classDef gate fill:#fff3cd,stroke:#664d03,stroke-width:2px;
    classDef check fill:#d1e7dd,stroke:#0f5132,stroke-width:2px;
    classDef final fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;

    class UIUX,Arch,Domain,MultiAgent gate;
    class DesignerReview,ArchitectReview,DomainReview,SupervisorReview check;
    class MergeGate,Ship final;
```

---

## 7. Quy trình Figma-to-Code & Vòng lặp Visual QA tự động
Trực quan hóa luồng đồng bộ biến thiết kế (Figma variables) thành mã nguồn dưới sự giám sát nghiêm ngặt của Linter và bộ test so sánh Visual Regression:

```mermaid
flowchart TD
    Fig["Figma Designs / Variables"] -->|Export JSON| Tokens["Tokens.json (Color, Spacing, Typography)"]
    Fig -->|Export Layout| Layout["Layout Blueprint JSON"]
    Tokens & Layout -->|Đầu vào nghiêm ngặt| Agent["Coding Agent Sandbox"]
    Agent -->|Tạo mã nguồn| Linter{"Tailwind/CSS Linter Check"}
    Linter -->|Fail: Có Class tự chế / Hardcoded color| LintErr["Báo lỗi linter & Trích xuất dòng code"]
    LintErr -->|Feedback| Agent
    Linter -->|Pass: Chỉ dùng classes token| Render["Playwright Headless Browser Render"]
    Render -->|Chụp Screenshot| RealImg["Giao diện thực (Actual Screen)"]
    Fig -->|Figma API Export Screenshot| DesignImg["Bản thiết kế mẫu (Baseline Screen)"]
    RealImg & DesignImg -->|Pixel Match Compare| DiffCheck{"So sánh Visual Diff > 0.5%?"}
    DiffCheck -->|Có lệch| DiffImg["Tạo Ảnh Diff Tô Đỏ Lỗi + Sai Spacing CSS"]
    DiffImg -->|Feedback trực quan| Agent
    DiffCheck -->|Không lệch| SignOff{"Designer Portal Review (HITL)"}
    SignOff -->|Từ chối| SignReject["Ghi log feedback hình ảnh & comment"]
    SignReject -->|Feedback| Agent
    SignOff -->|Duyệt| MergePR["Master Merge PR & Deploy"]
```

---

## 8. Kiến trúc Điều phối Multi-Agent song song hướng Domain (DDMA)
Mô hình chạy song song các Agent lập trình mà vẫn bảo vệ tính toàn vẹn của logic, ranh giới domain và tự động giải quyết các xung đột tích hợp:

```mermaid
flowchart TB
    Supervisor["Supervisor Agent"] -->|Phân rã Specs & ADR| OwnershipMap["Task Ownership Map"]
    
    subgraph Isolation["Không gian cách ly (Workspace Isolation)"]
        WorktreeA["Git Branch & Worktree A<br/>(Chỉ được phép sửa /src/modules/billing/)"]
        WorktreeB["Git Branch & Worktree B<br/>(Chỉ được phép sửa /src/modules/customer/)"]
    end
    
    OwnershipMap -->|Gán & khóa thư mục sửa đổi| WorktreeA
    OwnershipMap -->|Gán & khóa thư mục sửa đổi| WorktreeB
    
    SchemaLock[("Database Schema Locked<br/>(Không được sửa schema DB)")] -.-> Isolation
    
    subgraph Registry["Shared Contract Registry"]
        APISpec["API Specs (OpenAPI/GraphQL)"]
        EventSpec["Event Schemas (Avro)"]
    end
    
    WorktreeA & WorktreeB <-->|Tuân thủ contract| Registry
    
    WorktreeA -->|Đẩy code| CI_GateA["Branch CI A (Pact Contract Tests & Unit tests)"]
    WorktreeB -->|Đẩy code| CI_GateB["Branch CI B (Pact Contract Tests & Unit tests)"]
    
    CI_GateA & CI_GateB --> MasterGate{"Master CI & Integration Gate"}
    
    MasterGate -->|Xung đột contract / API fail| DebateRoom["Agentic Debate Room (Supervisor-moderated)"]
    DebateRoom -->|Vòng 1: Đề xuất & Chia sẻ context| DebateRoom
    DebateRoom -->|Vòng 2: Căn chỉnh tự động specs| DebateRoom
    DebateRoom -->|Vòng 3: Cập nhật code tương thích| DebateRoom
    
    DebateRoom -->|Giải quyết xong & tests pass| MasterGate
    DebateRoom -->|Thất bại sau 3 vòng| TechLead["Technical Lead HITL Checkpoint"]
    
    MasterGate -->|Pass all E2E & Contract tests| MasterMerge["Master Merge & Release"]
```
```

---

> **Nguyên tắc cốt lõi của bản đồ:**
> 1. **Con người nắm giữ ý định & cấu trúc:** Con người chịu trách nhiệm duyệt Spec, Kiến trúc (ADR), chuẩn giao diện (UI system) và hợp đồng module (Contracts).
> 2. **AI Agent thực thi trong ràng buộc:** Agent tự hoạt động, viết code, sửa lỗi và thực hiện quy trình tự động trong phạm vi các hộp chất lượng và sandbox được thiết lập sẵn.
> 3. **Vòng lặp đóng khép kín:** Mọi hành vi sai lệch trong vận hành (drift) hoặc sự cố sản phẩm đều là đầu vào để cải tiến hệ thống eval và huấn luyện/cải tiến kỹ năng của Agent một cách tự động.
